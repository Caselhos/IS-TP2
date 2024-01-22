from csv import DictReader


class CSVReader:

    def __init__(self, path, delimiter=','):
        self._path = path
        self._delimiter = delimiter

    def loop(self):
        with open(self._path, 'r', encoding="utf8") as file:
            for row in DictReader(file, delimiter=self._delimiter):
                yield row
        file.close()

    def read_entities(self, get_keys, builder, after_create=None):
        entities = {}
        for row in self.loop():

            keys = get_keys(row)
            if isinstance(keys, str):
                keys = [keys]

            for e in keys:
                if e not in entities:
                    entities[e] = builder(row)
            if after_create is not None:
                after_create(keys, row)
        return entities
