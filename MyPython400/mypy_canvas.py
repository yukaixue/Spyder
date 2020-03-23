# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:36:03 2020

@author: Administrator
"""

import tkinter as tk
import random

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
        '''创建登陆界面的组件'''
        
        self.canvas = tk.Canvas(self, width=300, height=200, bg='green')
        self.canvas.pack()
        #画一条直线
        self.canvas.create_line(10, 10, 30, 20, 40, 50)
        #画一个矩形
        self.canvas.create_rectangle(50, 50, 100, 120)
        #画一个矩形内接椭圆，坐标为边界矩形        
        self.canvas.create_oval(50, 50, 100, 120)
        
        global photo
        photo = tk.PhotoImage(file='timg.gif')
        self.canvas.create_image(150, 150, image=photo)
        
        tk.Button(self, text='画10个椭圆', command=self.drawOval).pack(side='left')
        
    def drawOval(self):
        for i in range(10):
            x1 = random.randrange(int(self.canvas['width'])/2)
            y1 = random.randrange(int(self.canvas['height'])/2)
            x2 = x1 + random.randrange(int(self.canvas['width'])/2)
            y2 = y1 + random.randrange(int(self.canvas['height'])/2)
            self.canvas.create_oval(x1, y1, x2, y2)

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
