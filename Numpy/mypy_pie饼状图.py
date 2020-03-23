# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:12:46 2020

@author: Administrator
"""

import matplotlib.pyplot as plt


#全国男女比例数据
man = 71351
woman = 68187
man_perc = man/(man+woman)
woman_perc = woman/(man+woman)
#添加名称
labels = ['男', '女']
#添加颜色
colors=['blue', 'red']
#绘制饼状图  pie
paches, texts, autotexts = plt.pie([man_perc, woman_perc], labels=labels, colors=colors, explode=(0.0, 0.05), autopct='%0.1f%%')
#设置饼状图中的字体颜色
for text in autotexts:
    text.set_color('white')
 #设置所有字体大小   
for text in texts+autotexts:
    text.set_fontsize(20)
plt.show()