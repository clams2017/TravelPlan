#!/usr/bin/env python
#-*- coding: utf-8 -*-

import configparser
import mysql.connector

from module.Spot import Spot


_config = configparser.ConfigParser()
_config.read('development.cfg')
_ACCOUNT = _config['MySQL']


class Storer(object):
    '''stores spot metadata into MySQL database.

    usage:
        with Storer() as storer:
            spots = ...
            storer.store(spots)
    or
        storer = Storer()
        storer.connect()
        storer.store(spots)
        storer.close()
    '''

    JALAN = 'jalan'
    GURUTABI = 'gurutabi'

    def __init__(self, account=_ACCOUNT):
        self.account = account

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def connect(self):
        self.conn = mysql.connector.connect(
          db      = self.account['db'],
          host    = self.account['host'],
          user    = self.account['user'],
          passwd  = self.account['passwd'],
          charset = 'utf8')

    def close(self):
        self.conn.close()

    def insert_spot(self, spot):
        cur = self.conn.cursor()
        q = 'INSERT INTO spot \
             (name, description, genre_id, lon, lat, image, access_text, address_code) \
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        for id in spot.oreore_genre_id:
            cur.execute(q, ( \
                spot.name, \
                spot.description, \
                id, \
                spot.lon, \
                spot.lat, \
                spot.image, \
                spot.access_text, \
                spot.address_code \
            ))
        self.conn.commit()
        cur.close()

    def store(self, spots):
        for spot in spots:
            self.insert_spot(spot)

    def map_oreoere_and_jalan(self, genre_small):
        return self.__map_oreoere_and_sites(genre_small, Storer.JALAN)

    def map_oreoere_and_gurutabi(self, genre_small):
        return self.__map_oreoere_and_sites(genre_small, Storer.GURUTABI)

    def __map_oreoere_and_sites(self, genre_small, site_name):
        cur = self.conn.cursor()
        q = 'SELECT {0}_genre.oreore_genre_id \
             FROM {0}_genre NATURAL JOIN {0}_genre_small \
             WHERE genre_small=%s'.format(site_name)
        cur.execute(q, (str(genre_small), ))
        itr = cur.fetchall()
        cur.close()
        return sorted([x[0] for x in itr])

    def find_same_spot(self, spot, oreore_genre_id):
        cur = self.conn.cursor()
        q = 'SELECT * FROM spot \
             WHERE lat BETWEEN %s AND %s \
               AND lon BETWEEN %s AND %s \
               AND genre_id=%s'
        cur.execute(q, (spot.lat - 0.005, spot.lat + 0.005,
            spot.lon - 0.005, spot.lon + 0.005, oreore_genre_id))
        r = cur.fetchall()
        cur.close()
        return r

    def resolve_pref_code(self, address_name):
        # 頭文字が2文字以上被る件が無いのでバリデーションする
        if len(address_name) < 2:
            return
        cur = self.conn.cursor()
        q = 'SELECT address.code \
             FROM address \
             WHERE address.name LIKE %s'
        cur.execute(q, (str(address_name)+'%',))
        itr = cur.fetchall()
        cur.close()
        # 都道府県データの性質上1件しかヒットしないため、LIKE検索で最初にヒットしたもののみ返却する
        pref = itr[0]
        return pref[0]
