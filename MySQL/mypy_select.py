# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 22:27:35 2020

@author: Administrator
"""

#导入模块
import pymysql


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
    psd = cur.fetchall()
    
    print(psd)
    print('查询数据成功')
except Exception as e:
    print(e)
    con.rollback()
    print('查询数据失败')
finally:
    #关闭连接
    con.close()