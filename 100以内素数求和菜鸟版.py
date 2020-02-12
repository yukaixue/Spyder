# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:13:58 2020

@author: Administrator
"""

import time
start = time.perf_counter()
Sum = 0
a = [i for i in range(101)]
b = [i for i in range(101)]
for i in range(2,100):
    for j in range(2,100):
        if i%j==0:
            if i!=j:
                break
            else:
                if i in a:
                    a.remove(i)
for item in a:
    b.remove(item)
for i in b:
    Sum +=i
print(Sum)
print(time.perf_counter()-start)