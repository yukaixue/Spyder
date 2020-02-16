# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:54:58 2020

@author: Administrator
"""

import requests
import time
from lxml import etree


def get_html(url):
    '''
    获得 HTML
    '''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/53\
        7.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return


def get_infos(html):
    '''
    提取数据
    '''
    html = etree.HTML(html)
    # 提取所有的大学标签信息
    ls = html.xpath('//tr[@class="alt"]')
    for info in ls:
        # 排名
        rank = info.xpath('./td[1]/text()')[0]
        # 学校名
        name = info.xpath('./td[2]/div/text()')[0]
        # 省份
        province = info.xpath('./td[3]/text()')[0]
        # 总分
        score = info.xpath('./td[4]/text()')[0]
        data = {
            '排名' : rank,
            '校名' : name,
            '省份' : province,
            '总分' : score,
        }
        print(data)


def main():
    '''
    主接口
    '''
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = get_html(url)
    get_infos(html)
    time.sleep(1)


if __name__ == '__main__':
    main()