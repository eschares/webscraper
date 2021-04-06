# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:30:45 2021

@author: eschares

https://realpython.com/beautiful-soup-web-scraper-python/
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

#print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')

print(results.prettify())

job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    print(job_elem, end='\n'*2)