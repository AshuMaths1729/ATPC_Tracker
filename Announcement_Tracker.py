#-*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:12:56 2019

@author: Ashutosh Agrahari
"""

import timeit
from bs4 import BeautifulSoup
import urllib.request
import csv

urlpage = 'https://www.amity.edu/placement/default.asp'

page = urllib.request.urlopen(urlpage)
soup = BeautifulSoup(page, 'html.parser')

table = soup.find('ul', attrs={'class':'notices black-list'})
results = table.find_all('li')
rows = []
rows.append(['Company Name', 'Link'])
#print("Upcoming Companies for recruitment..\n")
for result in results:
    data = str(result.find_all('strong'))
    a = str(result.find_all('a')[0])
    l = len(data)
    s = data[9:l - 10]
    sbar_ind = 0
    ss = a.split(' ')
    link = 'https://www.amity.edu/placement/' + ss[2][6:][:-1]
    rows.append([s, link])


with open('ATPC_Track.csv','w',newline='') as f_op:
    csv_op = csv.writer(f_op)
    csv_op.writerows(rows)
