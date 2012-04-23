#!/usr/bin python
# -*- coding: UTF-8 -*-

import os

from sqlalchemy.exc import DBAPIError

from bottle import debug, route, template, run, static_file

from functions import getdatetime, get_companies
from config import PROJECT_PATH, DEBUG, MAIN_TITLE

debug(DEBUG)

@route('/')
def index():
    page_title = "Kezdő oldal - {0}".format(MAIN_TITLE)
    css_files = ['/static/style.css', '/static/style_.css']
    js_files = []
    now = getdatetime()
    return template('index', page_title=page_title, css_files=css_files, js_files=js_files, now=now)
    
@route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='./static')
    
@route('/companies')
def companies():
    page_title = "Cégek - {0}".format(MAIN_TITLE)
    css_files = ['/static/style.css', '/static/style_.css']
    js_files = []
    now = getdatetime()
    companies = []
    errors = []
    try:
        companies = get_companies()
    except DBAPIError as e:
        if DEBUG:
            print(e.message)
            errors = ["Nem sikerült csatlakozni az adatbázishoz! :("]
    
    return template('companies', page_title=page_title, css_files=css_files, js_files=js_files, now=now, errors=errors, companies=companies)
    
@route('/company-details')
def companies():
    page_title = "Cég részletei - {0}".format(MAIN_TITLE)
    css_files = ['/static/style.css', '/static/style_.css']
    js_files = []
    now = getdatetime()
    return template('company-details', page_title=page_title, css_files=css_files, js_files=js_files, now=now)
    
run(host='localhost', port='80', reloader=True)