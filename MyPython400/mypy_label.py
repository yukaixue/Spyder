# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 22:28:22 2020

@author: Administrator
"""

import tkinter as tk

class Application(tk.Frame):
    '''一个经典的GUI程序的类的写法'''
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry('400x300')
        self.master.title('经典的GUI程序类的测试')
        self.pack()
        
        self.creatWidget()
        
    def creatWidget(self):
        '''创建组件'''
        self.label01 = tk.Label(self, text='百战程序员', width=10, height=2,
                             bg='green', fg='white')
        self.label01.pack()
        
        self.label02 = tk.Label(self, text='余开学', width=10, height=2,
                                bg='blue', fg='white', font=('黑体', 30))
        self.label02.pack(side='top')
        
        #显示图像
        #global photo
        self.photo = tk.PhotoImage(file='timg.gif')
        self.label03 = tk.Label(self, image=self.photo)
        self.label03.pack()
        
        #多行文本
        self.label04 = tk.Label(self, text='北京尚学堂\n百战程序员\n老高好帅，就是做饭不行',
                                borderwidth=1, fg='red', relief='solid', justify='center')
        self.label04.pack()
        

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()