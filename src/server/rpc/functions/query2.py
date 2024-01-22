import psycopg2


# Query using XPath to retrieve album information by title
def listarAlbumTitulo(titulo,filename):
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(user="is",
                                    password="is",
                                    host="db-xml",
                                    port="5432",
                                    database="is")

        cursor = connection.cursor()
        query = """
                SELECT xpath('//Xml/Albums/Album[ALBUMINFO[@name="%s"]]', xml)
                FROM imported_documents
                WHERE file_name = %s
            """
        filename = "'"+filename+"'"
        print(filename)
        query_param = query % (titulo, filename)

        cursor.execute(query_param)

        result = cursor.fetchall()
        return result
    except (Exception, psycopg2.Error) as error:
        print("Failed to fetch data", error)
        return error

    finally:
        if connection:
            cursor.close()
            connection.close()

