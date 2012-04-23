#!/usr/bin python
# -*- coding: UTF-8 -*-

import os
import ConfigParser

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

config = ConfigParser.ConfigParser()
config.read(PROJECT_PATH + '/pyszoftlab5.cfg')

DEBUG = config.get('debug_settings', 'mode')
