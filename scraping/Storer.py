#!/usr/bin/env python
#-*- coding: utf-8 -*-

import configparser
import mysql.connector

from Spot import Spot


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
             (name, description, genre_id, lon, lat, image, access_text) \
             VALUES (%s, %s, %s, %s, %s, %s, %s)'
        for id in spot.oreore_genre_id:
            cur.execute(q, ( \
                spot.name, \
                spot.description, \
                id, \
                spot.lon, \
                spot.lat, \
                spot.image, \
                spot.access_text \
            ))
        self.conn.commit()
        print('inserted: %s' % spot)
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
        cur.execute(q, (genre_small, ))
        itr = cur.fetchall()
        cur.close()
        return sorted([x[0] for x in itr])
