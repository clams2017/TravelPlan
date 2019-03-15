class OreoreSpot(object):
    def __init__(self, name, description, oreore_genre_id, \
            lon, lat, image, access_text):
        self.name = name[:128]
        self.description = description[:128]
        self.oreore_genre_id = oreore_genre_id
        self.lon = lon
        self.lat = lat
        self.image = image[:256]
        self.access_text = access_text[:256]
