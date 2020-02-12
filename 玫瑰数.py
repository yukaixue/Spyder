# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:14:38 2020

@author: Administrator
"""

for i in range(1000,10000):
    a = list(str(i))
    Sum = 0
    for n in range(4):
        Sum += pow(eval(a[n]),4)
    if i == Sum:
        print('{}'.format(i))