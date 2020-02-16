# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 23:11:39 2020

@author: Administrator
"""

import requests
import re
from lxml import etree
from fake_useragent import UserAgent


def get_html(url):
    '''
    请求网页
    :param url:
    :return:
    '''
    count = 0 # 计数请求了几次
    while True:
        headers = {
            'User-Agent' : UserAgent().random,
            'Cookie' : 'bid=v22EcJw6yqs; douban-fav-remind=1; __gads=ID=edec8f2750ea1826:T=1581580182:S=ALNI_MbzvT5AutKJUZNopCTAWoZGKlYAcA; __utmz=30149280.1581580187.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; gr_user_id=d7c8d3b4-c0c5-48fa-a1ef-a758eb1ed7d2; _vwo_uuid_v2=DF15F49EBA59B5D0314935D4CB6753DAA|adaeec63a65b556ea1b7dfca0d1e2989; viewed="1770782_25862578"; ll="118254"; _pk_ses.100001.4cf6=*; __utma=30149280.1834443378.1581580187.1581858196.1581863031.3; __utmb=30149280.0.10.1581863031; __utma=223695111.573654987.1581863031.1581863031.1581863031.1; __utmb=223695111.0.10.1581863031; __utmc=223695111; __utmz=223695111.1581863031.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __yadk_uid=X64bWEBbBNbBYquZz739F5QXbdw6arfp; _pk_id.100001.4cf6=808cb1039eeb1a50.1581863031.1.1581865251.1581863031.'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response
        else:
            count += 1
            if count == 2:
                return
            continue


def get_comments(response):
    '''
    提取评论
    :param response:
    :return:
    '''
    comments = re.findall(r'<span class=\\"short\\">(.*?)</span>',response.text,re.S)
    for comment in comments:
        try:
            print(eval(u"'" + comment + "'"))
            print('\n')
        except:
            pass
    pass


if __name__ == '__main__':
    urls = ['https://movie.douban.com/subject/27010768/comments?start={}&limit=20&sort=new_score&status=P&comments_only=1'
            .format(str(i)) for i in range(0,30,20)]
    for url in urls:
        response = get_html(url)
        get_comments(response)
        pass