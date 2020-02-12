# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:13:07 2020

@author: Administrator
"""

import time
start = time.perf_counter()
def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
sum = 0
for i in range(2,100):
    if is_prime(i):
        sum += i
print(sum)
print(time.perf_counter()-start)