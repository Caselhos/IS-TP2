import sys
import time
import pika
import psycopg2
from psycopg2 import OperationalError
import lxml
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as Soup
POLLING_FREQ = int(sys.argv[1]) if len(sys.argv) >= 2 else 60

# rabbitmqconfig
RABBITMQ_HOST = "rabbitmq"
RABBITMQ_PORT = 5672
RABBITMQ_QUEUE = "fila_tarefas"
RABBITMQ_VHOST = "is"


def print_psycopg2_exception(ex):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()

    # get the line number when exception occured
    line_num = traceback.tb_lineno

    # print the connect() error
    print("\npsycopg2 ERROR:", ex, "on line number:", line_num)
    print("psycopg2 traceback:", traceback, "-- type:", err_type)

    # psycopg2 extensions.Diagnostics object attribute
    print("\nextensions.Diagnostics:", ex.diag)

    # print the pgcode and pgerror exceptions
    print("pgerror:", ex.pgerror)
    print("pgcode:", ex.pgcode, "\n")


def callback(ch, method, properties, body):
    message = body.decode('utf-8')
    # Lógica para verificar a mensagem e executar a função correspondente
    if "Migrate the file:" in message:
        process_new_migration(message)
    else:
        print(f"Message not recognized: {message}")

def process_new_migration(mensagem):
    conn_xml = psycopg2.connect(host='db-xml', database='is', user='is', password='is')
    print(f"Processing: {mensagem}")

    filename = mensagem.split()

    cursor = conn_xml.cursor()
    # !TODO: 2- Execute a SELECT queries with xpath to retrieve the data we want to store in the relational db
    query = """
                        SELECT xpath('//Xml/Musics', xml)
                        FROM imported_documents
                        WHERE file_name = %s
                    """
    filenamestr = "'" + filename[-1] + "'"
    query_param = query % filenamestr

    cursor.execute(query_param)
    result = cursor.fetchall()
    for x in result:
        rea = ''.join(x)
        print(rea)
        soup = Soup(rea, "xml")
        print(soup.prettify())
        print(soup.Music['id'])
        #test = str(result).strip('[]')

    # !TODO: 3- Execute INSERT queries in the destination db


    # !TODO: 4- Make sure we store somehow in the origin database that certain records were already migrated.
    #          Change the db structure if needed.
    #cursor = conn_xml.cursor()
    #cursor.execute(
    #    "UPDATE public.imported_documents_documents (processed)VALUES (%s) where file_name=%s",
    #    (True,filename[-1])
    #)
    #db_org.commit()
    conn_xml.close()


if __name__ == "__main__":

    db_org = psycopg2.connect(host='db-xml', database='is', user='is', password='is')
    db_dst = psycopg2.connect(host='db-rel', database='is', user='is', password='is')
    while True:
        # Connect to both databases
        db_org = None
        db_dst = None
        try:
            print("Checking updates...")
            credentials = pika.PlainCredentials('is', 'is')
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=RABBITMQ_HOST,virtual_host=RABBITMQ_VHOST, port=RABBITMQ_PORT, credentials=credentials)
            )
            channel = connection.channel()
            channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
            channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)
            channel.start_consuming()
            db_org = psycopg2.connect(host='db-xml', database='is', user='is', password='is')
            db_dst = psycopg2.connect(host='db-rel', database='is', user='is', password='is')
        except OperationalError as err:
            print_psycopg2_exception(err)

        if db_dst is None or db_org is None:
            continue


        db_org.close()
        db_dst.close()

        time.sleep(POLLING_FREQ)
