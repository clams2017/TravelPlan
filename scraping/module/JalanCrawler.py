# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from time import sleep

from module.Crawler import Crawler
from module.Storer import Storer


class JalanCrawler(Crawler):

    def __init__(self):
        super().__init__()

    def navigate_search_result(self, url):
        # pager5ページ目までを探索対象とする
        # whileループ内でリクエストを飛ばすのは危険なため
        urls = []
        pager = [url] + ['%spage_%d/' % (url, i) for i in range(2, 6)]
        for page in pager:
            try:
                bs = self.parse_url(page)
                items = bs.findAll('div', class_='item-listContents')
                urls.extend(['https:' + i.findAll('a')[2]['href'] for i in items])
            except requests.exceptions.HTTPError as e:
                break
        return urls

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

    def extract_address_name(self, bs):
        return bs.find('dl', class_='c-area')\
                .findAll('div', class_='dropdownCurrent')[0].find('a').string
