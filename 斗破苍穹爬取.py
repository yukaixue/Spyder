# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:38:04 2020

@author: Administrator
"""

import requests
import re
from fake_useragent import UserAgent


def get_html(url):
    '''
    请求 html
    :return:
    '''
    headers = {
        'User-Agent' : UserAgent().random
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return


def get_info(html):
    '''
    提取文章标题
    :param html:
    :return:
    '''
    pat = '<dd> <a style="" href="/book/390/\d+.html">(.*?)</a></dd>'
    titles = re.findall(pat,html,re.S)
    for title in titles:
        print(title)


if __name__ == '__main__':
    '''
    主接口
    '''
    url = 'https://www.qu.la/book/390/'
    html = get_html(url)
    if html == None:
        print('请求失败！')
    get_info(html)