#!/usr/bin python
# -*- coding: UTF-8 -*-

import os

from sqlalchemy.exc import DBAPIError

from bottle import debug, route, template, run, static_file, get, post, request

from functions import getdatetime, get_companies, get_company_details
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
def companies_get():
    page_title = "Cégek - {0}".format(MAIN_TITLE)
    css_files = ['/static/style.css', '/static/style_.css']
    js_files = []
    now = getdatetime()
    companies = []
    errors = []
    
    prepost = {'nev': "", 'bankszamla': "", 'kapcsolattarto': "", 'operator': 'AND'}
    
    try:
        companies, _ = get_companies()
    except DBAPIError as e:
        if DEBUG:
            print(e.message)
            errors = ["Nem sikerült csatlakozni az adatbázishoz! :("]
    
    return template('companies', page_title=page_title, css_files=css_files, js_files=js_files, now=now, errors=errors, prepost=prepost, companies=companies)
    
@route('/companies', method='POST')
def companies_post():
    page_title = "Cégek - {0}".format(MAIN_TITLE)
    css_files = ['/static/style.css', '/static/style_.css']
    js_files = []
    now = getdatetime()
    companies = []
    errors = []
        
    nev = request.forms.get('nev')
    bankszamla = request.forms.get('bankszamla')
    kapcsolattarto = request.forms.get('kapcsolattarto')
    operator = request.forms.get('operator')
    
    if DEBUG:
        print("POST -- nev: {0}, bankszamla: {1}, kapcsolattarto: {2}, operator: {3}".format(nev, bankszamla, kapcsolattarto, operator))
    
    try:
        companies, prepost = get_companies(nev=nev, bankszamla=bankszamla, kapcsolattarto=kapcsolattarto, operator=operator)
    except DBAPIError as e:
        if DEBUG:
            print(e.message)
            errors = ["Nem sikerült csatlakozni az adatbázishoz! :("]
        
    return template('companies', page_title=page_title, css_files=css_files, js_files=js_files, now=now, errors=errors, companies=companies, prepost=prepost)

    
@route('/company-details/<id:int>')
def companies(id):
    page_title = "Cég részletei - {0}".format(MAIN_TITLE)
    css_files = ['/static/style.css', '/static/style_.css']
    js_files = []
    now = getdatetime()
    company = []
    errors = []
    try:
        company = get_company_details(id)[0]
    except DBAPIError as e:
        if DEBUG:
            print(e.message)
            errors = ["Nem sikerült csatlakozni az adatbázishoz! :("]
    except IndexError:
        company = []
        errors = ["Nincs ilyen azonosítóval rendelkező cég az adatbázisban! :("]
        
    return template('company-details', page_title=page_title, css_files=css_files, js_files=js_files, now=now, errors=errors, company=company)
    
run(host='localhost', port='80', reloader=True)