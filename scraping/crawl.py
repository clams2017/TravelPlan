#! /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import configparser

from module.Spot import Spot
from module.Storer import Storer


JALAN = 'jalan'
GURUTABI = 'gurutabi'


def main():
    args = parse_arg()
    cfg = parse_cfg()

    if args.site == JALAN:
        from module.JalanCrawler import JalanCrawler
        crawler = JalanCrawler()
        path = cfg['jalan_url_list']
    elif args.site == GURUTABI:
        from module.GurutabiCrawler import GurutabiCrawler
        crawler = GurutabiCrawler()
        path = cfg['gurutabi_url_list']

    if args.spot:
        spots = [crawler.fetch_detail(args.spot)]
        crawler.close()
    else:
        url_list = read_targets(path)
        spots = []
        for url in url_list:
            spots.extend(crawler.crawl(url))
        crawler.close()

    with Storer() as storer:
        for spot in spots:
            print('found a spot: %s' % spot)
            updated_genre = []
            for genre_id in spot.oreore_genre_id:
                same_spot = storer.find_same_spot(spot, genre_id)
                if not same_spot:
                    updated_genre.append(genre_id)
                    print('[name="%s", genre_id=%d] will be inserted.' \
                        % (spot.name, genre_id))
                else:
                    storer.increment_ref_count(same_spot[0][0])  # same_spot[\d+][0] is spot.id
                    print('[name="%s", genre_id=%d] is already existed.' \
                        % (spot.name, genre_id))
            spot.oreore_genre_id = updated_genre
            storer.insert_spot(spot)


def parse_arg():
    parser = argparse.ArgumentParser( \
        description=None)
    parser.add_argument('site', choices=[JALAN, GURUTABI], \
        help=None)
    parser.add_argument('-s', '--spot', default=None, \
        help=None)
    return parser.parse_args()


def parse_cfg():
    cfg = configparser.ConfigParser()
    cfg.read('development.cfg')
    return cfg['Crawler']


def read_targets(path):
    with open(path, 'r') as f:
        urls = []
        for line in f:
            urls.append(line.strip())
    return urls


if __name__ == '__main__':
    main()
