# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:15:29 2020

@author: Administrator
"""

import turtle,time,random
def drawGap():
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年',font=('Arail',18,'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=('Arail',18,'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=('Arail',18,'normal'))
        else:
            drawDigit(eval(i))
def main():
    turtle.title('来自学学的爱')
    turtle.setup(800,400,200,200)
    turtle.ht()
    turtle.penup()
    turtle.fd(-300)
    turtle.left(90)
    turtle.fd(100)
    turtle.right(90)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    n=-50
    turtle.goto(-350,n)
    turtle.colormode(255)
    if time.strftime('%Y-%m=%d+',time.gmtime()) == '2020-02=14+':
        for i in '亲爱的星星，亲爱的老婆：今天是情人节，祝你情人节快乐哟，余大傻永远爱你，么么哒！':
            RGB = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            turtle.pencolor(RGB)
            time.sleep(0.2)
            turtle.write(i,font=('Arial',22,'normal'))
            turtle.fd(30)
            if turtle.pos()[0] > 350:
                n=n-50
                turtle.goto(-350,n)                 
    else:
        for i in '亲爱的星星，亲爱的老婆：希望你天天开心，老公永远爱你哟！':
            RGB = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            turtle.pencolor(RGB)
            time.sleep(0.2)
            turtle.write(i,font=('Arial',22,'normal'))
            turtle.fd(30)
            if turtle.pos()[0] > 350:
                n=n-50
                turtle.goto(-350,n)
    turtle.hideturtle()
    turtle.done()
main()