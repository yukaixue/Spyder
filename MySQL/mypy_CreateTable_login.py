# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:19:33 2020

@author: Administrator
"""

#导入pymysql
import pymysql


#创建连接
con = pymysql.connect(host='localhost', user='root', password='11530114', database='python_db', port=3306)
#创建游标对象
cur = con.cursor()
#编写创建表的sql
sql='''
    create table login(
    num int primary key auto_increment,
    username varchar(30) not null,
    password varchar(30)
    )
'''
try:
    #执行创建表的sql
    cur.execute(sql)
    print('创建成功')
except Exception as e:
    print(e)
    print('创建失败')
finally:
    #关闭连接
    con.close()