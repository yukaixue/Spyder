# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:43:44 2020

@author: Administrator
"""

fo = open('output.txt','w+')
ls = ['中国','美国','法国']
fo.writelines(ls)
fo.seek(0)
for line in fo:
    print(line)
fo.close()