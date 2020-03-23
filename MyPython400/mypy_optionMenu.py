# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:29:09 2020

@author: Administrator
"""

import tkinter as tk


root = tk.Tk()
root.geometry('500x300')
root.title('OptionMenu测试')
root['bg'] = 'red'

f = tk.Frame(root, width=200, height=200, bg='blue')
f.pack()

v = tk.StringVar(f)
v.set('百战程序员')
om = tk.OptionMenu(f, v, '尚学堂', '百战程序员', '卓越班【保底18万】')
om['width'] = 20
om.pack()

def test1():
    print('最喜爱的机构:', v.get())
    v.set('请选择')
    
tk.Button(f, text='确定', width=10, command=test1).pack()

root.mainloop()
