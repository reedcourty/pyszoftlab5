#!/usr/bin python
# -*- coding: UTF-8 -*-

import datetime

from sqlalchemy import create_engine
from sqlalchemy.exc import DBAPIError

from config import DEBUG, DB_DIALECT, DB_SERVER, DB_USER, DB_PASSWD, DB_NAME

def getdatetime():
    return datetime.datetime.today().strftime("%Y.%m.%d. %H:%M:%S")

def is_valid(input):
    import string
    valid_chars = string.letters + string.digits + " öüóőúéáűíÖÜÓŐÚÉÁŰÍ.-"
    valid = True;

    for char in input:
        if not (char in valid_chars):
            valid = False;
            break
    
    return valid;
    
def create_query_from_search(nev, bankszamla, kapcsolattarto, operator):
    operator = operator.upper();
    query = "SELECT id, nev, kapcsolattarto FROM cegek "
    if ((nev != '') or (bankszamla != '') or (kapcsolattarto != '')):
        query = query + "WHERE "
        if ((nev != '') and is_valid(nev)):
            query = query + "nev LIKE '%{0}%' {1} ".format(nev, operator)
        if (bankszamla != ''):
            import re
            valid = re.search(r"^[\d]{1,10}$", bankszamla)
            if (valid != None):
                query = query + "bankszamla LIKE '%{0}%' {1} ".format(bankszamla, operator)
        if ((kapcsolattarto != '') and is_valid(kapcsolattarto)):
            query = query + "kapcsolattarto LIKE '%{0}%' {1} ".format(kapcsolattarto, operator)
        if query.endswith(operator + " "):
            query = query[:-(len(operator)+1)]
        if query.endswith('WHERE '):
            query = query[:-(len('WHERE '))]
        
    query = query + "ORDER BY nev;"
    
    if DEBUG:
        print(query)
    
    return query
    
def get_companies(nev='', bankszamla='', kapcsolattarto='', operator='AND'):
    companies = []
    
    query = create_query_from_search(nev=nev, bankszamla=bankszamla, kapcsolattarto=kapcsolattarto, operator=operator)

    if DEBUG:
        print(u"Kapcsolódás ({0}://{1}:{2}@{3}/{4})...".format(DB_DIALECT, DB_USER, DB_PASSWD, DB_SERVER, DB_NAME))
    
    engine = create_engine("{0}://{1}:{2}@{3}/{4}".format(DB_DIALECT, DB_USER, DB_PASSWD, DB_SERVER, DB_NAME))

    try:
        results = engine.execute(query)
    except DBAPIError as e:
        raise e
    
    for row in results:
        companies.append({'id': row.id, 'nev': row.nev, 'kapcsolattarto': row.kapcsolattarto})
    
    results.close()
    
    return companies
    
def get_company_details(id):
    company = []
    
    if DEBUG:
        print(u"Kapcsolódás ({0}://{1}:{2}@{3}/{4})...".format(DB_DIALECT, DB_USER, DB_PASSWD, DB_SERVER, DB_NAME))
    
    engine = create_engine("{0}://{1}:{2}@{3}/{4}".format(DB_DIALECT, DB_USER, DB_PASSWD, DB_SERVER, DB_NAME))

    query = "SELECT id, nev, bankszamla, kapcsolattarto FROM cegek WHERE id = ? ORDER BY nev;"
    try:
        results = engine.execute(query, id)
    except DBAPIError as e:
        raise e
    
    for row in results:
        company.append({'id': row.id, 'nev': row.nev, 'bankszamla': row.bankszamla, 'kapcsolattarto': row.kapcsolattarto})
    
    results.close()
    
    return company