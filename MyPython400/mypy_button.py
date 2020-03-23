# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 22:28:22 2020

@author: Administrator
"""

import tkinter as tk

class Application(tk.Frame):
    '''一个经典的GUI程序的类的写法'''
    
    def __init__(self, master='R'):
        super().__init__(master)
        self.master = master
        self.master.geometry('400x300')
        self.master.title('经典的GUI程序类的测试')
        self.pack()
        
        self.creatWidget()
        
    def creatWidget(self):
        '''创建组件'''
        self.btn01 = tk.Button(self, text='登录', fg='red', command=self.login )  #state='disabled'
        self.btn01.pack()
        
        self.photo = tk.PhotoImage(file='timg.gif')
        self.btn02 = tk.Button(self, image=self.photo, command=self.login)
        self.btn02.pack()
        #self.btn02.config(state='disabled')  #设置按钮为禁用
        
        
    def login(self):
        tk.messagebox.showinfo('尚学堂学习系统', '登陆成功！欢迎开始学习！')
        

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
