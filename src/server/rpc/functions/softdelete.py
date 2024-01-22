import psycopg2
from psycopg2 import sql


def softdelete(name_file_to_delete):
    global cursor
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(user="is",
                                      password="is",
                                      host="is-db",
                                      port="5432",
                                      database="is")

        with connection.cursor() as cursor:
            # add_column_query = sql.SQL(
            #     "ALTER TABLE {} ADD COLUMN IF NOT EXISTS is_deleted BOOLEAN DEFAULT FALSE;").format(
            #     sql.Identifier("imported_documents"))
            # cursor.execute(add_column_query)
            # connection.commit()

            delete_query = sql.SQL("UPDATE {} SET deleted_on = NOW() WHERE file_name = %s;").format(
                sql.Identifier("imported_documents"))
            cursor.execute(delete_query, (name_file_to_delete,))
            connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Failed to fetch data", error)
        return "Failed"

    finally:
        if connection:
            connection.close()

    return "Success"
