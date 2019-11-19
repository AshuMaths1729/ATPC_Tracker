from tkinter import *
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
#rows.append(['Company Name', 'Link'])
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
txt = "" 
rows[0][0]
for row in rows:
    cmp = row[0]
    link = row[1]
    txt += (cmp + " | " + link + "\n")

from tkinter import scrolledtext

window = Tk()
window.title("ATPC Track")
window.geometry('1366x768')
#lbl = Label(window, text=txt)
t = scrolledtext.ScrolledText(window,width=600, height=400)
t.insert(INSERT,txt)
t.grid(column=0, row=0)
window.mainloop()
"""
from tkinter import *
 
from tkinter import scrolledtext
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
txt = scrolledtext.ScrolledText(window,width=40,height=10)
 
txt.grid(column=0,row=0)
 
window.mainloop()
"""