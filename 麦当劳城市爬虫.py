# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:53:57 2020

@author: Administrator
"""

import requests
import re
import time
import csv
from fake_useragent import UserAgent


def create_csv_header():
    '''
    创建 csv，并写入第一行头信息
    :return:
    '''
    with open('mc.csv','a',encoding='utf-8',newline='') as f:
        # 创建写入对象
        writer = csv.writer(f)
        # 写入第一行头信息
        writer.writerow(['city','shop_name'])


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
    return infos

def write_csv(data):

    with open('mc.csv','a+',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        for str in data:
            writer.writerow(str)


if __name__ == '__main__':
    '''
    主接口
    '''
    mc_url = ['https://www.mcdonalds.com.cn/index/Quality/publicinfo/deliveryinfo?page={}'
                       .format(str(i)) for i in range(1,10)]
    create_csv_header() # 创建 csv ，并写入第一行头信息
    for url in mc_url:
        html = get_html(url)
        data = info(html)
        write_csv(data) # 写入 csv
        time.sleep(1)