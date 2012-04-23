#!/usr/bin python
# -*- coding: UTF-8 -*-

import os
import ConfigParser

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

config = ConfigParser.ConfigParser()
config.read(PROJECT_PATH + '/pyszoftlab5.cfg')

DEBUG = config.get('debug_settings', 'mode')

DB_SERVER = config.get('database_settings', 'server')
DB_DIALECT = config.get('database_settings', 'dialect')
DB_NAME = config.get('database_settings', 'name')
DB_USER = config.get('database_settings', 'user')
DB_PASSWD = config.get('database_settings', 'password')
