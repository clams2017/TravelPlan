#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import GurutabiSpot
from time import sleep
from bs4 import BeautifulSoup


def main():
    targets = read_targets()
    results = []
    for target in targets:
        spots = crawl(target)
        for spot in spots:
            results.append(spot)
    # insert to DB


def read_targets():
    files = open('gurutabi_urls', 'r')
    urls = []
    for line in files:
        urls.append(line)
    files.close()
    return urls


def crawl(url):
    print("fetch list: " + url)
    urls = fetch_urls(url)
    spots = []
    for url in urls:
        print("fetch spot: https:" + url)
        gurutabi_spot = fetch_spot(url)
        # detect genre
        ## genre_id = detect(spot)
        spots.append(gurutabi_spot.convert())
    return spots


def fetch_urls(url):
    # for
    sleep(1)
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    bs = BeautifulSoup(r.text, 'html.parser')
    items = bs.find('ul', class_='list-group-main-list').findAll('li')
    urls = []
    for item in items:
        urls.append(item.find('a').get("href"))
    return urls


def fetch_spot(url):
    sleep(1)
    r = requests.get("https:" + url)
    r.encoding = r.apparent_encoding
    bs = BeautifulSoup(r.text, 'html.parser')
    name = extract_name(bs)
    description = extract_description(bs)
    latitude = extract_latitude(bs)
    longitude = extract_longitude(bs)
    genre_small = extract_genre(bs, "gs")
    genre_middle = extract_genre(bs, "gm")
    image = extract_image(bs)
    access_text = extract_access_text(bs)
    return GurutabiSpot.GurutabiSpot(name, description, latitude, longitude, genre_small, genre_middle, image,
                                     access_text)


def extract_name(bs):
    return bs.find('h1', class_='main-content__headline').string.strip()


def extract_description(bs):
    mt40s = bs.findAll('div', class_='mt40')
    for mt40 in mt40s:
        sections = mt40.findAll('h2', class_='item-section-heading')
        for section in sections:
            if section.string == '概要':
                return mt40.find('p').string


def extract_latitude(bs):
    return bs.find('div', class_='access-map mt40').find('input', id='latitudeValue').get('value')


def extract_longitude(bs):
    return bs.find('div', class_='access-map mt40').find('input', id='longitudeValue').get('value')


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
        return ""
    return bxslider.find('img').get('src')


def extract_access_text(bs):
    access = bs.find('div', class_='access-map mt40')
    access_text = access.find('p', class_='access-map__txt')
    access_array = []
    for access_string in access_text.strings:
        access_array.append(access_string.strip())
    return '\n'.join(access_array).strip()


if __name__ == '__main__':
    main()
