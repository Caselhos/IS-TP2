import psycopg2


def listarTitulo():
    global cursor
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(user="is",
                                    password="is",
                                    host="db-xml",
                                    port="5432",
                                    database="is")

        cursor = connection.cursor()
        cursor.execute("""SELECT xpath('//Xml/Musics/Music[@id < 10 and @album_ref < 10]',"xml") 
        from "imported_documents"  where "file_name" ='aa4dbf77-f498-4bdf-a71f-47b191a54098.xml'; """)

        result = cursor.fetchall()

        for coluna in result:
            print(coluna[0])

        return result
    except (Exception, psycopg2.Error) as error:
        print("Failed to fetch data", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

listarTitulo()