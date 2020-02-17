# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:11:18 2020

@author: Administrator
"""

import requests
import re
import time
import pymysql
from fake_useragent import UserAgent

conn = pymysql.connect(host='localhost', user='root', password='11530114',
                       database='mydb', port=3306, charset='utf8')
# 创建游标
cursor = conn.cursor()


def get_html(url):
    '''
    下载 html
    :param url:
    :return:
    '''
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return


def info(html):
    '''
    解析麦当劳响应，获取数据
    :param response:
    :return:
    '''
    pat1 = '<span>城市</span>(.*?)</td>'
    cities = re.findall(pat1,html,re.S)

    pat2 = '<span>门店名称</span>(.*?)</td>'
    shop_names = re.findall(pat2,html,re.S)
    
    for i in range(len(cities)):
        cities[i] = cities[i].replace(' ','')
        shop_names[i] = shop_names[i].replace(' ','')

    infos = zip(cities,shop_names)
    return list(infos)


def insert_mysql(data):
    '''
    插入数据到数据库
    :param data:
    :return:
    '''
    for d in data:
        cursor.execute(
            'insert into mc(city,name) VALUES("%s","%s")' % (
            d[0],d[1]))
        # 从游标中获取结果
        cursor.fetchall()

        # 提交结果
        conn.commit()


if __name__ == '__main__':
    '''
    主接口
    '''
    mc_url = ['https://www.mcdonalds.com.cn/index/Quality/publicinfo/deliveryinfo?page={}'
                       .format(str(i)) for i in range(1,20)]
    for url in mc_url:
        html = get_html(url)
        data = info(html)
        insert_mysql(data)
        time.sleep(1)

    # 关闭游标
    cursor.close()

    # 关闭数据库
    conn.close()