# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:18:06 2020

@author: Administrator
"""

import tkinter as tk


class Application(tk.Frame):
    '''一个经典的GUI程序的类的写法'''
    
    def __init__(self, master='R'):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatWidget()
        
    def creatWidget(self):
        '''place布局，扑克牌出牌'''
        self.photo = tk.PhotoImage(file='timg.gif')
        #self.pukes = [tk.Label(self.master, image=self.photo) for i in range(10)]
        for i in range(10):
            self.puke = tk.Label(self.master, image=self.photo)
            self.puke.place(x=10+i*50, y=50)
            
        #为所有的puke增加事件处理
        self.puke.bind_class('Label', '<Button-1>', self.chupai)
            
    def chupai(self, event):
        print(event.widget.winfo_geometry())
        print(event.widget.winfo_y())
        
        if event.widget.winfo_y() == 50:
            event.widget.place(y=30)
        else:
            event.widget.place(y=50)
        

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('600x220')
    root.title('创建登陆界面的组件')
    root['bg'] = 'red'
    app = Application(root)
    root.mainloop()
