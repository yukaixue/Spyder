# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:50:42 2020

@author: Administrator
"""

import tkinter as tk


root = tk.Tk()
root.geometry('300x200')
root.title('滑块测试')
root['bg'] = 'red'

f = tk.Frame(root, width=200, height=200, bg='blue')
f.place(x=50, y=100)

def test1(value):
    print('滑块的值:', value)
    newFont = ('宋体', value)
    a.config(font=newFont)
    
s1 = tk.Scale(f, from_=10, to=60, length=200, tickinterval=10, orient='horizontal', command=test1)
s1.pack()

a = tk.Label(root, text='余开学', width=10, height=1, bg='blue', fg='white')
a.pack()

root.mainloop()
