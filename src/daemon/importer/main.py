import asyncio
import time
import uuid
import os

import psycopg2
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileCreatedEvent
from utils.csv_to_xml_converter import CSVtoXMLConverter

#todo a cena de dividir ficheiros em partes????
def get_csv_files_in_input_folder():
    return [os.path.join(dp, f) for dp, dn, filenames in os.walk(CSV_INPUT_PATH) for f in filenames if
            os.path.splitext(f)[1] == '.csv']


def generate_unique_file_name(directory):
    return f"{directory}/{str(uuid.uuid4())}.xml"


def convert_csv_to_xml(in_path, out_path):
    converter = CSVtoXMLConverter(in_path)
    file = open(out_path, "w", encoding="utf-8")
    file.write(converter.to_xml_str())


class CSVHandler(FileSystemEventHandler):
    def __init__(self, input_path, output_path):
        self._output_path = output_path
        self._input_path = input_path

        # generate file creation events for existing files
        for file in [os.path.join(dp, f) for dp, dn, filenames in os.walk(input_path) for f in filenames]:
            event = FileCreatedEvent(os.path.join(CSV_INPUT_PATH, file))
            event.event_type = "created"
            self.dispatch(event)

    async def convert_csv(self, csv_path):
        # here we avoid converting the same file again
        if csv_path in await self.get_converted_files():
            return

        print(f"new file to convert: '{csv_path}'")

        # we generate a unique file name for the XML file
        xml_path = generate_unique_file_name(self._output_path)

        # conversion
        convert_csv_to_xml(csv_path, xml_path)
        print(f"new xml file generated: '{xml_path}'")

        # dbconnection
        dbname = "is"
        user = "is"
        password = "is"
        host = "db-xml"
        port = "5432"
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()

        # update the converted_documents tables
        cursor.execute(
            "INSERT INTO public.converted_documents (src,file_size,dst)VALUES (%s, %s, %s)",
            (csv_path, os.path.getsize(xml_path), xml_path)
        )
        conn.commit()

        # store the XML document into the imported_documents table
        name = xml_path.removeprefix("/xml/")
        with open(xml_path, 'r', encoding="utf8") as file:
            xml_data = file.read()
        cursor.execute(
            "INSERT INTO public.imported_documents (file_name,xml)VALUES (%s, %s)",
            (name, xml_data)
        )
        conn.commit()

        # close dbconnection
        cursor.close()
        conn.close()

    async def get_converted_files(self):
        # retrieve from the database the files that were already converted before
        dbname = "is"
        user = "is"
        password = "is"
        host = "db-xml"
        port = "5432"

        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()

        # Execute the SELECT query with the specified parameters
        cursor.execute(
            "SELECT src FROM public.converted_documents"
        )
        test = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return test

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(".csv"):
            asyncio.run(self.convert_csv(event.src_path))


if __name__ == "__main__":
    CSV_INPUT_PATH = "/csv"
    XML_OUTPUT_PATH = "/xml"

    # create the file observer
    observer = Observer()
    observer.schedule(
        CSVHandler(CSV_INPUT_PATH, XML_OUTPUT_PATH),
        path=CSV_INPUT_PATH,
        recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
