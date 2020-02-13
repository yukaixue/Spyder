# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:30:31 2020

@author: Administrator
"""

import turtle
def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.screensize(600,600,'blue')
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color('white','white')
    turtle.begin_fill()
    for i in range(3):
        koch(400,3)
        turtle.right(120)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.done()
main()
    