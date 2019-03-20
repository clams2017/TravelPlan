# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from time import sleep

from Crawler import Crawler
from Storer import Storer


class JalanCrawler(Crawler):

    def __init__(self):
        super().__init__()

    # [TODO] スポット検索結果の2ページ目以降も探索する
    def navigate_search_result(self, url):
        bs = super().parse_url(url)
        items = bs.findAll('div', class_='item-listContents')
        return ['https:' + item.findAll('a')[2]['href'] for item in items]

    def detect_genre(self, genre):
        return self.storer.map_oreoere_and_jalan(genre)

    def extract_name(self, bs):
        return bs.find('h1', class_='detailTitle').string

    def extract_description(self, bs):
        gen = bs.find('div', id='aboutArea').find('p').strings
        return '\n'.join(super().strip_generator(gen))

    def extract_latitude(self, bs):
        return bs.find('div', id='detailMap-canvas')['data-lat']

    def extract_longitude(self, bs):
        return bs.find('div', id='detailMap-canvas')['data-lng']

    def extract_genre(self, bs):
        return bs.find('dl', class_='c-genre')\
                 .findAll('div', class_='dropdownCurrent')[1].find('a').string

    def extract_image(self, bs):
        return 'http:%s' % \
                bs.find('div', class_='detailGallery_box galleryArea-image')\
                  .find('img')['src']

    def extract_access_text(self, bs):
        try:
            return bs.find('table', class_='basicInfoTable')\
                     .findAll('tr')[-1].find('td').string.strip()
        except AttributeError as e:
            return ''
