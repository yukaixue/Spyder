# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:48:29 2020

@author: Administrator
"""

f = open("data.csv")
ls = f.readlines()
ls = ls[::-1]
lt = []
for item in ls:
    item = item.strip("\n")
    item = item.replace(" ", "")
    lt = item.split(",")
    lt = lt[::-1]
    print(";".join(lt))
f.close()