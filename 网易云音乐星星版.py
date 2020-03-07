# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:07:19 2020

@author: Administrator
"""


import tkinter as tk
import os
from urllib.request import urlretrieve
from selenium import webdriver


def get_music_name():
    
root = tk.Tk()
root.title('网易云音乐---星星专用版')
root.geometry('430x350')

label = tk.Label(root,text='请输入下载歌曲：',font=('华文行楷',18))
label.grid()

entry = tk.Entry(root,font=('隶书',16))
entry.grid(row=0,column=1)

text = tk.Listbox(root,font=('隶书',20),width=30,heigh=10)
text.grid(row=1,columnspan=2)

button = tk.Button(root,text='下载歌曲',font=('隶书',15))
button.grid(row=2,column=0,sticky='W')

button1 = tk.Button(root,text='退出程序',font=('隶书',15),command=root.quit)
button1.grid(row=2,column=1,sticky='E')

#https://music.163.com/#/search/m/?s=%E6%99%B4%E5%A4%A9&type=1


















root.mainloop()
