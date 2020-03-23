# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:14:57 2020

@author: Administrator
"""


import tkinter as tk


root = tk.Tk()
root.geometry('530x300')
root.title('event事件测试')
root['bg'] = 'red'

c1 = tk.Canvas(root, width=200, height=200, bg='green')
c1.pack()


def mouseTest(event):
    print('鼠标左键单击位置(相对于父容器):{},{}'.format(event.x, event.y))
    print('鼠标左键单击位置(相对于屏幕):{},{}'.format(event.x_root, event.y_root))
    print('事件绑定的组件:{}'.format(event.widget))
    
def testDrag(event):
    c1.create_oval(event.x, event.y, event.x+10, event.y+10)
    
def keyboradTest(event):
    print('键的keycode:{},键的char:{},键的keysym:{}'.format(event.keycode, event.char, event.keysym))
    
def press_a_test(event):
    print('press a')
    
def release_a_test(event):
    print('release a')


c1.bind('<Button-1>', mouseTest)
c1.bind('<B1-Motion>', testDrag)

root.bind('<KeyPress>', keyboradTest)
root.bind('<KeyPress-a>', press_a_test)
root.bind('<KeyRelease-a>', release_a_test)

root.mainloop()

    


 