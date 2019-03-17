#! /usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import requests
from time import sleep
from bs4 import BeautifulSoup

from GurutabiSpot import GurutabiSpot
from Storer import Storer


_config = configparser.ConfigParser()
_config.read('development.cfg')
URL_LIST = _config['Crawler']['gurutabi_url_list']


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
        print('fetch spot: https:' + url)
        spot = fetch_spot(url)
        # detect genre
        ids = storer.map_oreoere_and_sites(spot.genre_small, Storer.GURUTABI)
        for id in ids:
            spots.append(spot.convert(id))
    return spots


def fetch_urls(url):
    # for safe usage in roop
    sleep(1)
    bs = parse_html(url)
    items = bs.find('ul', class_='list-group-main-list').findAll('li')
    return [item.find('a').get('href') for item in items]


def fetch_spot(url):
    # for safe usage in roop
    sleep(1)
    bs = parse_html('https:' + url)
    name = extract_name(bs)
    description = extract_description(bs)
    latitude = extract_latitude(bs)
    longitude = extract_longitude(bs)
    genre_small = extract_genre(bs, 'gs')
    genre_middle = extract_genre(bs, 'gm')
    image = extract_image(bs)
    access_text = extract_access_text(bs)
    return GurutabiSpot(name, description, genre_small, genre_middle, \
                        longitude, latitude, image, access_text)


def parse_html(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    bs = BeautifulSoup(r.text, 'html.parser')
    return bs


def extract_name(bs):
    return bs.find('h1', class_='main-content__headline').string.strip()


def extract_description(bs):
    mt40s = bs.findAll('div', class_='mt40')
    for mt40 in mt40s:
        sections = mt40.findAll('h2', class_='item-section-heading')
        for section in sections:
            if section.string == u'概要':
                list_ = mt40.find('p').strings
                return '\n'.join(list_)


def extract_latitude(bs):
    return bs.find('div', class_='access-map mt40')\
             .find('input', id='latitudeValue').get('value')


def extract_longitude(bs):
    return bs.find('div', class_='access-map mt40')\
             .find('input', id='longitudeValue').get('value')


def extract_genre(bs, type_):
    breadcrumbs = bs.find('ol', class_='breadcrumb__list').findAll('li')
    for breadcrumb in breadcrumbs:
        a = breadcrumb.find('a')
        if not a:
            continue
        url = a.get('href')
        paths = url.split('/')
        if paths[-2].startswith(type_):
            return a.string


def extract_image(bs):
    bxslider = bs.find('ul', class_='bxslider')
    if not bxslider:
        return ''
    return bxslider.find('img').get('src')


def extract_access_text(bs):
    access = bs.find('div', class_='access-map mt40')
    access_text = access.find('p', class_='access-map__txt')
    access_list = strip_generator(access_text)
    return '\n'.join(access_list).strip()


def strip_generator(generator):
    list_ = []
    for v in generator:
        if isinstance(v, str):
            list_.append(v.strip())
    return list_


if __name__ == '__main__':
    main()
