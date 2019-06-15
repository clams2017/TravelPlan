class Spot(object):
    def __init__(self, *, \
            name, description, oreore_genre_id=[], sites_genre_name, \
            lon, lat, image, access_text, address_code):
        self.name = name[:128]
        self.description = description[:1024]
        self.oreore_genre_id = oreore_genre_id
        self.sites_genre_name = sites_genre_name
        self.lon = lon
        self.lat = lat
        self.image = image[:256]
        self.access_text = access_text[:256]
        self.address_code = address_code[:11]

    def __repr__(self):
        return '''
<Spot(
    name="%s",
    description="%s",
    oreore_genre_id="%s",
    sites_genre_name="%s",
    lon="%s", lat="%s",
    image="%s",
    access_text="%s",
    address_code="%s"
)>''' % ( \
                self.name, self.description, self.oreore_genre_id, \
                self.sites_genre_name, self.lon, self.lat, \
                self.image, self.access_text, self.address_code)
