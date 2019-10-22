class Spot(object):
    def __init__(self, *, \
            name, description, oreore_genre_id=[], sites_genre_name, \
            lon, lat, image, access_text, address_code):
        self.name = name[:128]
        self.description = description[:1024]
        self.oreore_genre_id = oreore_genre_id
        self.sites_genre_name = sites_genre_name
        self.image = image[:256]
        self.access_text = access_text[:256]
        self.address_code = address_code[:11]
        try:
            self.lon = round(float(lon), 2)
            self.lat = round(float(lat), 2)
        except:
            # エラー値を入れておくが、エラーの発生したスポットは全て同一判定される
            # TODO 緯度経度のないスポットの扱いの検討
            self.lon = -1
            self.lat = -1

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
