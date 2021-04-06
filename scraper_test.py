# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 21:31:31 2021

@author: eschares

https://www.youtube.com/watch?v=mKxFfjNyj3c
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#my_url = 'https://onlinelibrary.wiley.com/doi/abs/10.1111/1744-7917.12600'
page_html = open('C:/Users/eschares/Desktop/wiley_test.html')

#uClient = uReq(my_url)
#page_html = uClient.read()
#uClient.close()

page_soup = soup(page_html, 'lxml')
#print(page_soup.original_encoding)

containers = page_soup.findAll("div", {"class": "citation"})
print(containers)
#print(len(containers))
#print(soup.prettify(containers[0]))