# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:51:42 2020

@author: Administrator
"""

import requests
import time
from bs4 import BeautifulSoup
import lxml


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
        return response.text
    else:
        return


def get_infos(html):
    '''
    提取数据
    '''
    html = BeautifulSoup(html,'lxml')
    # 排名
    ranks = html.find_all('span',class_='pc_temp_num')
    # 歌手 + 歌名
    names = html.find_all('a',class_='pc_temp_songname')
    # 播放时间
    times = html.find_all('span',class_='pc_temp_time')

    # 打印信息
    for r,n,t in zip(ranks,names,times):
        r = r.get_text().replace('\n','').replace('\t','').replace('\r','')
        n = n.get_text()
        t = t.get_text().replace('\n','').replace('\t','').replace('\r','')
        print('{:^3} {:<30}{:>50}'.format(r,n,t))


def main():
    '''
    主接口
    '''
    urls = ['https://www.kugou.com/yy/rank/home/{}-6666.html?from=rank'
                .format(str(i)) for i in range(1, 2)]
    for url in urls:
        html = get_html(url)
        get_infos(html)
        time.sleep(1)


if __name__ == '__main__':
    main()