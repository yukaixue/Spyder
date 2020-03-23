# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:38:11 2020

@author: Administrator
"""

import tkinter as tk


root = tk.Tk()
root.geometry('270x30')
root.title('bind_class')

def mouseTest1(event):
    print('bind()方式绑定，可以获取event对象')
    print(event.widget)
    
def mouseTest2(a, b):
    print('a={},b={}'.format(a, b))
    print('command方式绑定，不能直接获取对event象')
    
def mouseTest3(event):
    print('右键单击事件，绑定给所有按钮啦！！')
    print(event.widget)
    

b1 = tk.Button(root, text='测试bind()绑定')
b1.grid(row=0, column=0, sticky='EW')
b1.bind('<Button-1>', mouseTest1)

b2 = tk.Button(root, text='测试command2', command=lambda:mouseTest2('余开学', '王星'))
b2.grid(row=0, column=1, sticky='EW')

b3 = tk.Button(root, text='空的')
b3.grid(row=0, column=2, sticky='EW')

root.bind_class('Button', '<Button-3>', mouseTest3)

root.mainloop()
