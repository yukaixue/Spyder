# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 09:50:15 2020

@author: Administrator
"""

fname = input('请输入需要打开的文件名称：')
fo = open(fname,'r',encoding='utf-8')
txt = fo.read()
print(txt)
fo.close()