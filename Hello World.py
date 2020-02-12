# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:05:47 2020

@author: Administrator
"""

Input_int = input()
Output = 'Hello World'
if eval(Input_int) == 0:
    print('Hello World')
elif eval(Input_int) > 0:
    for i in range(0,len(Output),2):
        print('{}'.format(Output[i:i+2]))
else:
    for i in range(len(Output)):
        print('{}'.format(Output[i]))