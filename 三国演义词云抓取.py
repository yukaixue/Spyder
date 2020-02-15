# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:59:52 2020

@author: Administrator
"""

import jieba
import wordcloud

txt = open('三国演义.txt', 'r', encoding='utf-8').read()
words = ' '.join(jieba.lcut(txt))
w = wordcloud.WordCloud(width=1000,font_path='msyh.ttc',\
                        height=700,max_words=20)
w.generate(words)
w.to_file('三国演义词云.png')