# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 21:41:50 2021

@author: eschares

https://medium.com/@raiyanquaium/how-to-web-scrape-using-beautiful-soup-in-python-without-running-into-http-error-403-554875e5abed
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

filename = "output.txt"
f = open(filename,'w')

#url = 'https://www.fool.ca/recent-headlines/'
url = 'https://onlinelibrary.wiley.com/doi/abs/10.1111/1744-7917.12600'
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")    #get the BS object

f.write(page_soup.prettify())
#print(page_soup.prettify())  #prints out formatted HTML version

#title = page_soup.find("icon-mail_outline")
#print(title)

#containers = page_soup.findAll("p","author-type")
containers = page_soup.findAll("div", {"class": "citation"})
print(len(containers))
#for container in containers:
#    print(container)