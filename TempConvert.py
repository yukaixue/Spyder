# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:34:58 2020

@author: Administrator
"""

#TempConvert.py
TempStr = input('请输入带有符号的温度值，如100C或者212F，这里输入：')
if TempStr[-1] not in ['F','f','C','c']:
    print('输入格式错误，请重新输入')
else:
    if TempStr[-1] in ['F','f']:
        C = (eval(TempStr[:-1]) - 32)/1.8
        print('转换后的温度是{:.2f}C'.format(C))
    elif TempStr[-1] in ['C','c']:
        C = 1.8*eval(TempStr[:-1]) + 32
        print('转换后的温度是{:.2f}F'.format(C))
