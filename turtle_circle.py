# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:21:20 2020

@author: Administrator
"""

import turtle as t


n = eval(input("n >= 3: "))
t.color('blue', 'yellow')
for i in range(3, n+2):
    t.begin_fill()
    if i < n+1:
        t.circle(50, steps=i)
        t.setheading(0)
        t.fd(100)
    else:
        t.circle(50)
    t.end_fill()
t.hideturtle()
t.done()