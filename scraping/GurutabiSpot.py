import OreoreSpot


class GurutabiSpot(object):
    def __init__(self, name, description, genre_small, genre_middle, lon, lat, image, access_text):
        self.name = name
        self.description = description
        self.genre_small = genre_small
        self.genre_middle = genre_middle
        self.lon = lon
        self.lat = lat
        self.image = image
        self.access_text = access_text

    def convert(self):
        return OreoreSpot.OreoreSpot(
            self.name,
            self.description,
            self.genre_small,
            self.lon,
            self.lat,
            self.image,
            self.access_text
        )
