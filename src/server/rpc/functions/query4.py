import psycopg2

# Query using XPath to retrieve music information by artist name

def listarMusicaArtista(artist,filename):
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
                    SELECT xpath('//Xml/Musics/Music[Artists/Artist/@id="%s"]', xml)
                    FROM imported_documents
                    WHERE file_name = %s
                """
        filename = "'" + filename + "'"
        print(filename)
        query_param = query % (artist, filename)

        cursor.execute(query_param)
        rows = cursor.fetchall()

        result = []
        for row in rows:
            result += row[0]  # assumes row[0] returns a list of music

        print("Musicas do artista: ", ''.join(result))

        return rows
    finally:
        if connection:
            cursor.close()
            connection.close()
