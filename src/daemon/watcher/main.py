import psycopg2
import pika
import os
import time

# dbconfig
dbname = "is"
user = "is"
password = "is"
host = "db-xml"
port = "5432"

# rabbitmqconfig
RABBITMQ_HOST = "rabbitmq"
RABBITMQ_PORT = 5672
RABBITMQ_QUEUE = "fila_tarefas"
RABBITMQ_VHOST = "is"

def connect_postgresql():
    try:
        conn = psycopg2.connect(
            host=host,port=port,database=dbname,user=user,password=password
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting PostgreSQL: {e}")
        return None

def connect_rabbitmq():
    try:
        credentials = pika.PlainCredentials('is', 'is')
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBITMQ_HOST, virtual_host=RABBITMQ_VHOST, port=RABBITMQ_PORT, credentials=credentials)
        )
        channel = connection.channel()
        channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
        return channel
    except Exception as e:
        print(f"Error connecting RabbitMQ: {e}")
        return None

def process_new_files():
    conn = connect_postgresql()
    if not conn:
        return
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT file_name FROM public.imported_documents WHERE processed = FALSE")
            results= cursor.fetchall()
            for result in results:
                file_name = result[0]
                # SEND MESSAGE TO RABBITMQ
                mensagem = f"Migrate the file: {file_name}"
                print(f"SENDING TO RABBITMQ - Migrate the file: {file_name}")
                canal_rabbitmq.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE, body=mensagem)
    except Exception as e:
        print(f"Error processing new files: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    while True:
        canal_rabbitmq = connect_rabbitmq()
        if canal_rabbitmq:
            process_new_files()
            canal_rabbitmq.close()

        # delay between checks
        time.sleep(10)
