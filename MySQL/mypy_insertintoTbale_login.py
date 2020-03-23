# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:09:45 2020

@author: Administrator
"""

#导入模块
import pymysql


#创建连接
con = pymysql.connect(host='localhost', user='root', password='11530114', database='python_db', port=3306)
#创建游标对象
cur = con.cursor()
#编写插入数据的sql
sql = 'insert into login(username, password) values(%s, %s)'
try:
    #执行sql
    cur.execute(sql, ('13343454693', 'ykx123456'))
    #提交事务
    con.commit()
    print('插入成功')
except Exception as e:
    print(e)
    con.rollback()
    print('插入失败')
finally:
    #关闭连接
    con.close()