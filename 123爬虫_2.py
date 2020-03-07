# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 09:57:17 2020

@author: Administrator
"""

from requests_html import HTMLSession


session = HTMLSession()
links = ['https://movie.douban.com/subject/1292052/', 'https://movie.douban.com/subject/1962665/', 'https://movie.douban.com/subject/26752088/']
for link in links:
    r = session.get(link)
    title = r.html.find('#content > h1 > span:nth-child(1)', first=True)
    year = r.html.find('#content > h1 > span.year', first=True)
    print(title.text, year.text)