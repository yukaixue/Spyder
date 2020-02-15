# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:10:13 2020

@author: Administrator
"""

import jieba
import wordcloud
import numpy as np
from PIL import Image


f = open('聊天记录.txt','r',encoding='utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = ' '.join(ls)

img=Image.open('black_mask.png')
mk=np.array(img)
w = wordcloud.WordCloud(mask=mk, font_path='msyh.ttc', mode='RGBA', \
                 background_color=None,stopwords={"Tiwo13",'Tiwo08','Tiwo09',\
                'Tiwo11','小猪',"Tiwo14","Tiwo16"},max_words=20).generate(txt)

w.to_file('聊天记录.png')


