# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 04:23:38 2020

@author: Ali
"""
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
##########Scrap China Corona Table
url='https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req)
html = response.read()
soup = BeautifulSoup(html)

tabulka = soup.find("table", {"class" : "wp-block-table aligncenter is-style-stripes"})

records = [] # store all of the records in this list
for row in tabulka.findAll('tr'):
    col = row.findAll('td')
    china = col[0].text.strip()
    cases = col[1].text.strip()
    deathes = col[2].text.strip()
    record = '%s;%s;%s' % (china, cases,deathes) # store the record with a ';' between prvy and druhy
    records.append(record)

dfChina=pd.DataFrame(records)
dfChina[['china','cases','deaths']] = dfChina[0].str.split(";",expand=True) 
dfChina=dfChina.drop([0],axis=1)

#Rename DF Headers
dfChina.columns = dfChina.iloc[0]
dfChina = dfChina[1:]

#Drop Total Row
dfChina=dfChina[:-1]


##########Scrap World Corona Table
url='https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req)
html = response.read()
soup = BeautifulSoup(html)
tabulka2 = soup.find("table", {"class" : "wp-block-table is-style-regular"})
recordsW = [] # store all of the records in this list
for row in tabulka2.findAll('tr'):
    col = row.findAll('td')
    china = col[0].text.strip()
    cases = col[1].text.strip()
    deathes = col[2].text.strip()
    record = '%s;%s;%s' % (china, cases,deathes) # store the record with a ';' between prvy and druhy
    recordsW.append(record)

dfWorld=pd.DataFrame(recordsW)
dfWorld[['country','cases','deaths']] = dfWorld[0].str.split(";",expand=True) 
dfWorld=dfWorld.drop([0],axis=1)

#Rename DF Headers
dfWorld = dfWorld[1:]

#Drop Total Row
dfWorld=dfWorld[:-1]