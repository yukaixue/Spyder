# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 09:09:16 2020

@author: Administrator
"""

import pymysql


class Mysql:
    "创建MySQL执行Tbale相关操作的类，创建表，插入数据，修改数据，查询数据"
    def __init__(self, host, user, password, database, port):
        self.con = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
        self.cur = self.con.cursor()
        
    def CreateTable(self, sql):
        try:
            #执行创建表的sql
            self.cur.execute(sql)
            print('创建成功')
        except Exception as e:
            print(e)
            print('创建失败')
    
    def Insert_Update_Delete(self, sql, data):
        try:
            #执行sql
            self.cur.execute(sql, data)
            #提交事务
            self.con.commit()
            print('执行成功')
        except Exception as e:
            print(e)
            self.con.rollback()
            print('执行失败')
    
    def Select(self, sql):
        try:
            #执行sql
            self.cur.execute(sql)
            #处理结果集
            data = self.cur.fetchall()
            print('查询数据成功')
        except Exception as e:
            print(e)
            self.con.rollback()
            print('查询数据失败')   
        return data

    def Close(self):
        #关闭连接
        self.con.close()        
    
        