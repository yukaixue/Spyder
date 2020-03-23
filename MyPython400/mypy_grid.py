# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:36:03 2020

@author: Administrator
"""

import tkinter as tk


class Application(tk.Frame):
    '''一个经典的GUI程序的类的写法'''
    
    def __init__(self, master='R'):
        super().__init__(master)
        self.master = master
        self.master.geometry('400x400')
        self.master.title('创建登陆界面的组件')
        self.pack()
        
        self.creatWidget()
        
    def creatWidget(self):
        '''通过grid布局实现登陆界面'''
        
        self.label01 = tk.Label(self, text='用户名')
        self.label01.grid(row=0, column=0)
        self.entry01 = tk.Entry(self)
        self.entry01.grid(row=0, column=1)
        tk.Label(self, text='用户名为手机号').grid(row=0, column=2)
        
        tk.Label(self, text='密码').grid(row=1, column=0)
        tk.Entry(self, show='*').grid(row=1, column=1)
        
        tk.Button(self, text='登录').grid(row=2, column=1, sticky='EW')
        tk.Button(self, text='取消').grid(row=2, column=2, sticky='E')
        
        
        

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
