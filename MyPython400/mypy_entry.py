# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:36:03 2020

@author: Administrator
"""

import tkinter as tk
import pymysql


def ver(user, pwd):
    #创建连接
    con = pymysql.connect(host='localhost', user='root', password='11530114', database='python_db', port=3306)
    #创建游标对象
    cur = con.cursor()
    #编写插入数据的sql
    sql = 'select * from login'
    try:
        #执行sql
        cur.execute(sql)
        #处理结果集
        items = cur.fetchall()
        dic = {}
        for i in range(len(items)):
            if items[i][1] not in dic:
                dic[items[i][1]] = items[i][2]
        if user in dic:
            if dic[user] == pwd:
                return True
        else:
            return False
        print('查询数据成功')
    except Exception as e:
        print(e)
        con.rollback()
        print('查询数据失败')
    finally:
        #关闭连接
        con.close()


class Application(tk.Frame):
    '''一个经典的GUI程序的类的写法'''
    
    def __init__(self, master='R'):
        super().__init__(master)
        self.master = master
        self.master.geometry('400x150')
        self.master.title('创建登陆界面的组件')
        self.pack()
        
        self.creatWidget()
        
    def creatWidget(self):
        '''创建登陆界面的组件'''
        
        self.label01 = tk.Label(self, text='用户名')
        self.label01.pack()
        
        #StringVar变量绑定到指定的组件
        #双向关联
        v1 = tk.StringVar()
        self.entry01 = tk.Entry(self, textvariable=v1)
        self.entry01.pack()
        v1.set('admin')
        
        #创建密码框
        self.label02 = tk.Label(self, text='密码')
        self.label02.pack()
        
        #StringVar变量绑定到指定的组件
        #双向关联
        v2 = tk.StringVar()
        self.entry02 = tk.Entry(self, textvariable=v2, show='*')
        self.entry02.pack()
        v2.set('')
        
        #创建登录按钮
        self.btn01 = tk.Button(self, text='登录', command=self.login)
        self.btn01.pack()
        
    def login(self):
        username = self.entry01.get()
        pwd = self.entry02.get()
        
        if ver(username, pwd):
            tk.messagebox.showinfo('尚学堂学习系统', '登陆成功！欢迎开始学习！')
        else:
            tk.messagebox.showinfo('尚学堂学习系统', '登陆失败！账号或密码错误！')
        

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
