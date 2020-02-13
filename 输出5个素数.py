# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:36:37 2020

@author: Administrator
"""
count = 0
pri = []
def prime(m):
    global count,pri
    def is_prime(n):
        for i in range(2,n):
            if n % i ==0:
                return False
        return True
    if is_prime(m):
        pri.append(str(m))
        count +=1
    if count < 5:
        prime(m+1)
    return pri
n = eval(input())
for item in prime(n):
    print(item,end=',')

            
            
        
            