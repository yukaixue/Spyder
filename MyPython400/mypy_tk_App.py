# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 22:28:22 2020

@author: Administrator
"""

import tkinter as tk

class Application(tk.Frame):
    '''一个经典的GUI程序的类的写法'''
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.geometry('400x100')
        self.master.title('经典的GUI程序类的测试')
        self.pack()
        
        self.creatWidget()
        
    def creatWidget(self):
        '''创建组件'''
        self.btn01 = tk.Button(self)
        self.btn01['text'] = '点我就送花'
        self.btn01.pack(side='top')
        self.btn01['command'] = self.songhua
        self.bunQuit = tk.Button(self.master, text='退出', fg='red', command=self.master.destroy)
        self.bunQuit.pack(side='bottom')
        
    def songhua(e):
        tk.messagebox.showinfo('送花','送你99朵花')
        

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()