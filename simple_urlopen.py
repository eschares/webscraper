# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 10:02:34 2021

@author: eschares

Web Scraping with Python, 2nd edition
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')

bs = BeautifulSoup(html.read(), 'lxml')
print(bs.h1)