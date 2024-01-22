import xml.etree.ElementTree as ET


class Artist:

    def __init__(self, name):
        Artist.counter += 1
        self._id = Artist.counter
        self._name = name

    def to_xml(self):
        el = ET.Element("Artist")
        el.set("id", str(self._id))
        el.set("name", self._name)
        return el

    def to_xml_embedded(self):
        el = ET.Element("Artist")
        el.set("id", str(self._id))
        return el

    def get_id(self):
        return self._id
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"


Artist.counter = 0
