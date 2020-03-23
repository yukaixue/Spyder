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
        self.pack()
        
        self.creatWidget()
        
    def creatWidget(self):
        '''实现计算器的界面'''
        
        btnText = (('MC', 'M+', 'M-', 'MR'),
                   ('C', '±', '÷', '×'),
                   (7, 8, 9, '-'),
                   (4, 5, 6, '+'),
                   (1, 2, 3, '='),
                   (0, '.'))
        
        tk.Entry(self).grid(row=0, column=0, columnspan=4, pady=10)
        
        for rindex, r in enumerate(btnText, start=1):
            for cindex, c in enumerate(r):
                if c == '=':
                    tk.Button(self, text=c, width=2).grid(row=rindex, column=cindex, sticky='NSEW', rowspan=2)
                elif c == 0:
                    tk.Button(self, text=c, width=2).grid(row=rindex, column=cindex, sticky='EW', columnspan=2)
                elif c == '.':
                    tk.Button(self, text=c, width=2).grid(row=rindex, column=cindex+1, sticky='EW')
                else:
                    tk.Button(self, text=c, width=2).grid(row=rindex, column=cindex, sticky='EW')
                    

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('150x220')
    root.title('创建登陆界面的组件')
    root['bg'] = 'red'
    app = Application(root)
    root.mainloop()
