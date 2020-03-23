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
        self.master.geometry('780x220')
        self.master.title('创建电子钢琴')
        self.pack()
        
        self.creatWidget()
        
    def creatWidget(self):
        '''创建文本'''
        
        btnText = ('流行风', '中国风', '日本风', '重金属', '轻音乐')
        
        for txt in btnText:
            tk.Button(self, text=txt).pack(side='left', padx='10')
        
        for i in range(1, 19):
            tk.Label(self.master, width=5, height=10, borderwidth=1, relief='solid',
                     bg='black' if i%2==0 else 'white').pack(side='left', padx=2)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
