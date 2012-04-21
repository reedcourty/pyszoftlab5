#!/usr/bin python
# -*- coding: UTF-8 -*-

import os
os.chdir(os.path.dirname(__file__))

from bottle import debug, route, template, run

debug(True)

@route('/')
def index():
    return template('index')
    
run(host='localhost', port='80')