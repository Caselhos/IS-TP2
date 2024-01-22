import psycopg2


def listarAlbumData(date,filename):
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

        # Use XPath in the SQL query to extract music information by artist name
        query = """
                        SELECT xpath('//Xml/Albums/Album/ALBUMINFO[@release_date="%s"]', xml)
                        FROM imported_documents
                        WHERE file_name = %s
                    """
        #se mudar o '=' para '<' ou '>' não printa direito

        filename = "'" + filename + "'"
        print(filename)
        query_param = query % (date, filename)
        cursor.execute(query_param)
        rows = cursor.fetchall()

        for row in rows:
            result = row[0]
            
            print("Album Info:", result)
        return rows
    finally:
        if connection:
            cursor.close()
            connection.close()

#listarAlbumData("2022-09-23")
