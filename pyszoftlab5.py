#!/usr/bin python
# -*- coding: UTF-8 -*-

import os

from functions import getdatetime
from config import PROJECT_PATH, DEBUG

from bottle import debug, route, template, run, static_file

debug(DEBUG)

@route('/')
def index():
    page_title = "Kezdő oldal - Nádudvari György (reedcourty) - Szoftver laboratórium 5 - 5. (egyébként PHP, de most Python) mérés"
    css_files = ['/static/style.css', '/static/style_.css']
    js_files = []
    now = getdatetime()
    return template('index', page_title=page_title, css_files=css_files, js_files=js_files, now=now)
    
@route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='./static')
    
@route('/companies')
def companies():
    page_title = "Cégek - Nádudvari György (reedcourty) - Szoftver laboratórium 5 - 5. (egyébként PHP, de most Python) mérés"
    css_files = ['/static/style.css', '/static/style_.css']
    js_files = []
    now = getdatetime()
    return template('companies', page_title=page_title, css_files=css_files, js_files=js_files, now=now)
    
@route('/company-details')
def companies():
    page_title = "Cég részletei - Nádudvari György (reedcourty) - Szoftver laboratórium 5 - 5. (egyébként PHP, de most Python) mérés"
    css_files = ['/static/style.css', '/static/style_.css']
    js_files = []
    now = getdatetime()
    return template('company-details', page_title=page_title, css_files=css_files, js_files=js_files, now=now)
    
run(host='localhost', port='80', reloader=True)