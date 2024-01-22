import xml.dom.minidom as md
import xml.etree.ElementTree as ET

from utils.csv_reader import CSVReader
from entities.album import Album
from entities.artist import Artist
from entities.country import Country
from entities.music import Music


class CSVtoXMLConverter:

    def __init__(self, path):
        self._reader = CSVReader(path)

    def to_xml(self):


        # read albums
        albums = self._reader.read_entities(
            get_keys=lambda row: row["album_name"],
            builder=lambda row: Album(
                name=row["album_name"],
                release_date=row["album_release_date"]
            )
        )


        # read countries
        countries = self._reader.read_entities(
            get_keys=lambda row: row["country"],
            builder=lambda row: Country(row["country"])
        )

        # read musics
        musics = self._reader.read_entities(
            get_keys=lambda row: row["name"],
            builder=lambda row: Music(
                spotify_id=row["spotify_id"],
                name=row["name"],
                album=albums[row["album_name"]]
            )
        )

        def after_creating_artist(artists, row):
            for artist in artists:
                musics[row["name"]].add_artist(artist)

        # read artists
        artists = self._reader.read_entities(
            get_keys=lambda row: row["artists"].replace(' ', '').split(","),
            builder=lambda row: Artist(row["artists"]), after_create=after_creating_artist

        )
        for y in musics.values():
            y._artists = list(set(y._artists))
        for x in artists.keys():
            artists[x].set_name(x)

        for z in musics.values():
            index=0
            for y in z.get_artists():
                for h in artists.values():
                    if h.get_name() == y:
                        z._artists[index]= h.get_id() # this is criminal
                        index=index+1

        """
        for x in days.values():
            x.add_data(musics)
        """


        # generate the final xml
        root_el = ET.Element("Xml")

        musics_el = ET.Element("Musics")
        for music in musics.values():
            musics_el.append(music.to_xml())

        countries_el = ET.Element("Countries")
        for country in countries.values():
            countries_el.append(country.to_xml())

        artists_el = ET.Element("Artists")
        for artist in artists.values():
            artists_el.append(artist.to_xml())

        albums_el = ET.Element("Albums")
        for album in albums.values():
            albums_el.append(album.to_xml())

        root_el.append(musics_el)
        root_el.append(artists_el)
        root_el.append(albums_el)
        root_el.append(countries_el)

        return root_el

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()
