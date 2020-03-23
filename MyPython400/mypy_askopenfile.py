# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:20:02 2020

@author: Administrator
"""

import tkinter as tk
from tkinter import filedialog



root = tk.Tk()
root.geometry('400x500')
root.title('文本选择')
root['bg'] = 'white'

f = tk.Frame(root, width=200, height=200, bg='blue')
f.place(x=50, y=100)

def test1():
    with filedialog.askopenfile(title='上传文件', initialdir='f:',
                                   filetypes=[('文本文件', '.txt')]) as f:
        show['text'] = f.read()

tk.Button(root, text='选择读取的文本文件', command=test1).pack()

show = tk.Label(f, width=40, height=20, bg='green') 
show.pack()   

root.mainloop()
