# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 21:07:49 2020

@author: Administrator
"""

import tkinter as tk


root = tk.Tk()


root.title('我的第一个GUI程序')
root.geometry('500x300+0+0')


btn01 = tk.Button(root)
btn01['text'] = '点我就送花'
btn01.pack()
def songhua(e):
    tk.messagebox.showinfo('Message', '送你一朵花')
    print('送你99朵花')


btn01.bind('<Button-1>', songhua)


root.mainloop()