# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 09:46:07 2020

@author: Administrator
"""

from requests_html import HTMLSession


session = HTMLSession()
r = session.get('https://movie.douban.com/subject/1292052/')
title = r.html.find('#content > h1 > span:nth-child(1)',first=True)
print(title.text)