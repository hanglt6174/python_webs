# -*- coding:utf-8 -*-

import ConfigParser
from peewee.peewee import *

config = ConfigParser.ConfigParser()
config.read('config/db.conf')

database = MySQLDatabase(
                            config.get('db', 'database'),
                             **{
                                 'charset': 'utf8',
                                 'use_unicode': True,
                                 'host': config.get('db', 'host'),
                                 'user': config.get('db', 'user'),
                                 'passwd': config.get('db', 'password')
                                }
                        )