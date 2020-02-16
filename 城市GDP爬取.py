# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:06:20 2020

@author: Administrator
"""

import requests
import re
from fake_useragent import UserAgent


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


def GDP_people_info(html):
    '''
    解析获得 GDP，人口的数据
    :param response:
    :return:
    '''
    pat = '<p>(\d+.*?)</p>'
    infos = re.findall(pat,html,re.S)

    # 处理提取的数据，以 [(城市，GDP，人数).....] 形式保存
    datas = []
    for info in infos:
        # 人数
        pat1 = r'.*?(\d+)万'
        people = re.findall(pat1,info)

        # GDP
        pat2 = r'(\d+)亿元，'
        GDP = re.findall(pat2,info)

        # 城市
        pat3 = r'\d+\.(.*?)\d+亿元，'
        city = re.findall(pat3,info)
        city = city[0].split('（')[0] + '市'

        try:
            datas.append((city,GDP[0],people[0]))
        except:
            pass

    return datas


if __name__ == '__main__':
    '''
    主接口
    '''
    url = 'http://caifuhao.eastmoney.com/news/20190201115604564011000'
    html = get_html(url)
    data = GDP_people_info(html)
    print(data)