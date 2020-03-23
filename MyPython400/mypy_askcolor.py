# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:04:01 2020

@author: Administrator
"""

import tkinter as tk



root = tk.Tk()
root.geometry('300x320')
root.title('颜色选择')
root['bg'] = 'white'

f = tk.Frame(root, width=200, height=200, bg='black')
f.place(x=50, y=100)

def test1():
    s1 = tk.colorchooser.askcolor(color='red', title='选择背景颜色')
    print(s1)
    f.config(bg=s1[1])

tk.Button(root, text='选择背景颜色', command=test1).pack()    

root.mainloop()
