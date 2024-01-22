import xml.etree.ElementTree as ET
from .artist import Artist

class Music:

    def __init__(self, spotify_id, name, album):
        Music.counter += 1
        self._id = Music.counter
        self._spotify_id = spotify_id
        self._name = name
        self._artists = []
        self._album = album

    def to_xml(self):
        el = ET.Element("Music")
        el.set("id", str(self._id))
        el.set("spotify_id", str(self._spotify_id))
        el.set("album_ref", str(self._album.get_id()))
        el.set("name", self._name)
        artists_el = ET.SubElement(el, "Artists")
        for artist in self._artists:
            art_el = ET.Element("Artist")
            art_el.set("id", str(artist))
            artists_el.append(art_el)
        return el

    def add_artist(self, artist):
        self._artists.append(artist)

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name
    def get_artists(self):
        return self._artists
    """
    def get_rank(self):
        return self._rank

    def get_country(self):
        return self._country
    """
    def __str__(self):
        return (f"{self._name}, spotify_id:{self._spotify_id}, country:{self._country}, "
                f"artist:{self._artists}, album:{self._album}")


Music.counter = 0
