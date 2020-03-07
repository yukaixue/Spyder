# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:32:16 2020

@author: Administrator
"""

import execjs
import requests
import os
import time
import re
import PyPDF2
from fake_useragent import UserAgent


def get_t():
    '''
    执行 JavaScript 代码生成参数 t
    '''
    with open(r'1.js') as f:
        s = f.read()
        s = execjs.compile(s)
        t = s.call('t')
        return t


def get_url(p):
    '''
    生成对应页数的 url
    '''
    url = 'http://sxqh.chineseall.cn/v3/book/content/fIPLg/pdf/{}?t={}'
    t = get_t()
    url = url.format(p,t)
    return url


def get_requests(url,p):
    '''
    请求 pdf url
    '''
    while True: # 请求失败，在请求一直成功为止
        try:
            headers = {'User-Agent' : UserAgent().random,
                       'Cookie' : 'JSESSIONID=DF207A8A8E8964D680DD733B533A6560; _Tvt5MJ89bV_=A9577ACE1D8E538E734AE16BA888C4EF45AB6CCC5272D0902251660D86210F41836CEE40CD0DB9C102CC0D54CCDD68B9258D339CE9A1B52AFB6C6D103E4BF00B565494A706613343CC75A04EDB72A342; LvGPHdwDRT=KMLTB7VVHFCDKEHWGUHXWT5AB25ISM7UIEF5TLZI4BAVPWHBVTFPLE7HJ7UKANMGS4OM6L3NX2UVLKVVCBTT6LI62IGGCDREZ66ICSI'
                       }
            response = requests.get(url,headers=headers)
            if response.status_code == 200:
                return response
        except:
            continue


def download_pdf(text,p):
    '''
    下载为 pdf，名称为页码
    '''
    with open(str(p) + '.pdf','wb') as f:
        f.write(text)
        print('第 %s 页下载成功，共 233 页。' % str(p))


def merge_pdf(name):
    '''
    合并 pdf
    '''
    print('正在合并最终 pdf')
    # find all the pdf files in current directory.
    mypath = os.getcwd()
    pattern = r"\.pdf$"
    file_names_lst = [mypath + "\\" + f for f in os.listdir(mypath) if re.search(pattern, f, re.IGNORECASE)
                      and not re.search(name+'.pdf', f)]

    # 对文件路径按页码排序
    dic = {}
    for i in range(len(file_names_lst)):
        page = re.findall(r'(\d+)\.pdf', file_names_lst[i])[0]
        dic[int(page)] = file_names_lst[i]
    file_names_lst = sorted(dic.items(), key=lambda x: x[0])
    file_names_lst = [file[1] for file in file_names_lst]

    # merge the file.
    opened_file = [open(file_name, 'rb') for file_name in file_names_lst]
    pdfFM = PyPDF2.PdfFileMerger()
    for file in opened_file:
        pdfFM.append(file)
        
    # output the file.
    with open(mypath + "\\" + name + ".pdf", 'wb') as write_out_file:
        pdfFM.write(write_out_file)

    # close all the input files.
    for file in opened_file:
        file.close()

    print('合并完成 %s' % name)
    
    #自动删除爬取的pdf
    for file_name in file_names_lst:
        os.remove(file_name)
    
    print('多余的pdf已经删除完毕')


def main():
    '''
    主逻辑
    '''
    start = time.time()
    for p in range(1,233): # 共有 446 也 pdf
        url = get_url(p) # 构造这一页的 url
        response = get_requests(url,p) # 请求 pdf 链接
        download_pdf(response.content,p) # 图片下载为 pdf
    end = time.time()
    print(end - start) # 打印下载总共用时
    merge_pdf(name='精通Scrapy网络爬虫') # 合并 pdf 文件，name 为电子书名


if __name__ == '__main__':
    main()