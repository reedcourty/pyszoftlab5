#!/usr/bin python
# -*- coding: UTF-8 -*-

import datetime

from sqlalchemy import create_engine
from sqlalchemy.exc import DBAPIError

from config import DEBUG, DB_DIALECT, DB_SERVER, DB_USER, DB_PASSWD, DB_NAME

def getdatetime():
    return datetime.datetime.today().strftime("%Y.%m.%d. %H:%M:%S")
    
def get_companies():
    companies = []
    
    if DEBUG:
        print("Kapcsolódás ({0}://{1}:{2}@{3}/{4})...".format(DB_DIALECT, DB_USER, DB_PASSWD, DB_SERVER, DB_NAME))
    
    engine = create_engine("{0}://{1}:{2}@{3}/{4}".format(DB_DIALECT, DB_USER, DB_PASSWD, DB_SERVER, DB_NAME))

    query = "SELECT nev, kapcsolattarto FROM cegek ORDER BY nev;"
    try:
        results = engine.execute(query)
    except DBAPIError as e:
        raise e
    
    for row in results:
        companies.append({'nev': row.nev, 'kapcsolattarto': row.kapcsolattarto})
    
    return companies