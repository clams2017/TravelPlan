#! /usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import requests
from time import sleep
from bs4 import BeautifulSoup

from JalanSpot import JalanSpot
from Storer import Storer


_config = configparser.ConfigParser()
_config.read('development.cfg')
URL_LIST = _config['Crawler']['jalan_url_list']


def main():
    targets = read_targets(URL_LIST)
    with Storer() as storer:
        for target in targets:
            results = crawl(target, storer)
            storer.store(results)


def read_targets(path):
    with open(path, 'r') as f:
        urls = []
        for line in f:
            urls.append(line.strip())
    return urls


def crawl(url, storer):
    print('fetch list: ' + url)
    urls = fetch_urls(url)
    spots = []
    for url in urls:
        print('fetch spot: http:' + url)
        spot = fetch_spot(url)
        # detect genre
        ids = storer.map_oreoere_and_sites(spot.genre_small, Storer.JALAN)
        for id in ids:
            spots.append(spot.convert(id))
    return spots


def fetch_urls(url):
    # for safe usage in roop
    sleep(1)
    bs = parse_html(url)
    items = bs.findAll('div', class_='item-listContents')
    return [item.findAll('a')[2]['href'] for item in items]


def fetch_spot(url):
    # for safe usage in roop
    sleep(1)
    bs = parse_html('http:' + url)
    name = extract_name(bs)
    description = extract_description(bs)
    latitude = extract_latitude(bs)
    longitude = extract_longitude(bs)
    genre_middle = extract_genre_middle(bs)
    genre_small = extract_genre_small(bs)
    image = extract_image(bs)
    access_text = extract_access_text(bs)
    return JalanSpot(name, description, genre_small, genre_middle, \
                        longitude, latitude, image, access_text)


def parse_html(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    bs = BeautifulSoup(r.text, 'html.parser')
    return bs


def extract_name(bs):
    return bs.find('h1', class_='detailTitle').string


def extract_description(bs):
    gen = bs.find('div', id='aboutArea').find('p').strings
    return '\n'.join(strip_generator(gen))


def extract_latitude(bs):
    return bs.find('div', id='detailMap-canvas')['data-lat']


def extract_longitude(bs):
    return bs.find('div', id='detailMap-canvas')['data-lng']


def extract_genre_middle(bs):
    return bs.find('dl', class_='c-genre')\
             .findAll('div', class_='dropdownCurrent')[0].find('a').string


def extract_genre_small(bs):
    return bs.find('dl', class_='c-genre')\
             .findAll('div', class_='dropdownCurrent')[1].find('a').string


def extract_image(bs):
    return 'http:%s' % \
            bs.find('div', class_='detailGallery_box galleryArea-image')\
              .find('img')['src']


def extract_access_text(bs):
    return bs.find('table', class_='basicInfoTable')\
             .findAll('tr')[1].find('td').string.strip()


def strip_generator(generator):
    list_ = []
    for v in generator:
        if isinstance(v, str):
            list_.append(v.strip())
    return list_


if __name__ == '__main__':
    main()
