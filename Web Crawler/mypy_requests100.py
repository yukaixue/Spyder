# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 09:27:18 2020

@author: Administrator
"""

import requests
import time


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '访问异常'


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    i = 0
    start = time.perf_counter()
    while i < 100:
        getHTMLText(url)
        i += 1
print('获取网页{}次，总耗时{}s'.format(i, time.perf_counter()-start))