# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 22:03:57 2021

@author: eschares

https://www.reddit.com/r/learnpython/comments/31cjbp/beautifulsoup_script_with_a_useragent_simply_does/
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import requests

url = 'https://onlinelibrary.wiley.com/doi/abs/10.1111/1744-7917.12600'
r = requests.get(url)
r.raise_for_status()
page_soup = soup(r, "html.parser")    #get the BS object
#html = r.text
#req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

#webpage = urlopen(req).read()
#page_soup = soup(webpage, "html.parser")    #get the BS object