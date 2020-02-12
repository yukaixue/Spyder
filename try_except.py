# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

try:
    num = eval(input('请输入一个整数：'))
    print(num**2)
except NameError:
    print('错误：输入的不是一个整数')