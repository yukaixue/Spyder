# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:54:19 2020

@author: Administrator
"""

import time
scale = 50
start = time.perf_counter()
print('执行开始'.center(scale//2,'-'))
for i in range(scale+1):
    a = i*'*'
    b = (scale-i)*'-'
    c = i/scale*100
    dur = time.perf_counter() - start
    print('\r{:^3.0f}%[{}->{}]{:3.2f}s'.format(c,a,b,dur),end = '')
    time.sleep(0.1)
print('\n'+'执行结束'.center(scale//2,'-'))