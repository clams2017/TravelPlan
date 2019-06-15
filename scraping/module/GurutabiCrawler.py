# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from time import sleep

from module.Crawler import Crawler
from module.Storer import Storer


class GurutabiCrawler(Crawler):

    def __init__(self):
        super().__init__()

    def navigate_search_result(self, url):
        # pager5ページ目までを探索対象とする
        # whileループ内でリクエストを飛ばすのは危険なため
        urls = []
        pager = [url] + ['%spg%d/' % (url, i) for i in range(2, 6)]
        for page in pager:
            try:
                bs = self.parse_url(page)
                items = bs.find('ul', class_='list-group-main-list').findAll('li')
                urls.extend(['https:' + i.find('a').get('href') for i in items])
            except requests.exceptions.HTTPError as e:
                break
        return urls

    def detect_genre(self, genre):
        return self.storer.map_oreoere_and_gurutabi(genre)

    def extract_name(self, bs):
        return bs.find('h1', class_='main-content__headline').string.strip()

    def extract_description(self, bs):
        mt40s = bs.findAll('div', class_='mt40')
        for mt40 in mt40s:
            sections = mt40.findAll('h2', class_='item-section-heading')
            for section in sections:
                if section.string == u'概要':
                    list_ = mt40.find('p').strings
                    return '\n'.join(list_)

    def extract_latitude(self, bs):
        return bs.find('div', class_='access-map mt40')\
                 .find('input', id='latitudeValue').get('value')

    def extract_longitude(self, bs):
        return bs.find('div', class_='access-map mt40')\
                 .find('input', id='longitudeValue').get('value')

    def extract_genre(self, bs):
        return self.__extract_breadcrumb(bs, 'gs')

    def extract_image(self, bs):
        bxslider = bs.find('ul', class_='bxslider')
        if not bxslider:
            return ''
        return 'http:%s' % bxslider.find('img').get('src')

    def extract_access_text(self, bs):
        access = bs.find('div', class_='access-map mt40')
        access_text = access.find('p', class_='access-map__txt')
        access_list = self.strip_generator(access_text)
        return '\n'.join(access_list).strip()

    def extract_address_name(self, bs):
        return self.__extract_breadcrumb(bs, 'p')

    def __extract_breadcrumb(self, bs, prefix):
        breadcrumbs = bs.find('ol', class_='breadcrumb__list').findAll('li')
        for breadcrumb in breadcrumbs:
            a = breadcrumb.find('a')
            if not a:
                continue
            url = a.get('href')
            paths = url.split('/')
            if paths[-2].startswith(prefix):
                return a.string
