# -*- coding: utf-8 -*-

import requests
import validators
from bs4 import BeautifulSoup
from copy import copy
from time import sleep

from module.Spot import Spot
from module.Storer import Storer


class Crawler(object):

    def __init__(self):
        self.storer = Storer()
        self.storer.connect()

    def close(self):
        self.storer.close()

    def crawl(self, search_query):
        print('fetch list: %s' % search_query)
        urls = self.navigate_search_result(search_query)
        spots = []
        for url in urls:
            print('fetch spot: %s' % url)
            spots.append(self.fetch_detail(url))
        return spots

    def fetch_detail(self, url_or_file):
        bs = self.parse_url_or_file(url_or_file)
        spot = self.navigate_detail_page(bs)
        ids = self.detect_genre(spot.sites_genre_name)
        spot.oreore_genre_id = ids
        return spot

    def navigate_detail_page(self, bs):
        name = self.extract_name(bs)
        description = self.extract_description(bs)
        sites_genre_name = self.extract_genre(bs)
        lat = self.extract_latitude(bs)
        lon = self.extract_longitude(bs)
        image = self.extract_image(bs)
        access_text = self.extract_access_text(bs)
        return Spot(name=name, description=description, \
            sites_genre_name=sites_genre_name, \
            lon=lon, lat=lat, image=image, access_text=access_text)

    def detect_genre(self, genre):
        raise NotImplementedError()

    def navigate_search_result(self, url):
        raise NotImplementedError()

    def extract_name(self, bs):
        raise NotImplementedError()

    def extract_description(self, bs):
        raise NotImplementedError()

    def extract_latitude(self, bs):
        raise NotImplementedError()

    def extract_longitude(self, bs):
        raise NotImplementedError()

    def extract_genre(self, bs):
        raise NotImplementedError()

    def extract_image(self, bs):
        raise NotImplementedError()

    def extract_access_text(self, bs):
        raise NotImplementedError()

    @staticmethod
    def parse_url_or_file(url_or_file):
        if validators.url(url_or_file):
            return Crawler.parse_url(url_or_file)
        else:
            return Crawler.parse_file(url_or_file)

    @staticmethod
    def parse_url(url):
        # for safe usage in loops
        sleep(30)
        r = requests.get(url)
        if not r.status_code == requests.codes.ok:
            r.raise_for_status()
        r.encoding = r.apparent_encoding
        bs = BeautifulSoup(r.text, 'html.parser')
        return bs

    @staticmethod
    def parse_file(file):
        with open(file) as f:
            bs = BeautifulSoup(f, 'html.parser')
        return bs

    @staticmethod
    def strip_generator(generator):
        list_ = []
        for v in generator:
            if isinstance(v, str):
                list_.append(v.strip())
        return list_
