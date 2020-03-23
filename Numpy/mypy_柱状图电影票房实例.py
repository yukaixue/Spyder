# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:03:47 2020

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np


#准备数据
#三部电影的名称
real_names = ['千与千寻', '玩具总动员4', '黑衣人：全球追击']
#3天内票房
real_num1 = [7548, 4013, 1673]
real_num2 = [5453, 1840, 1080]
real_num3 = [4384, 1520, 1000]
#绘制柱状图
x = np.arange(len(real_names))
width=0.2
plt.bar(x, real_num1, alpha=0.5, width=width, label=real_names[0])
plt.bar([i+width for i in x], real_num2, alpha=0.5, width=width, label=real_names[1])
plt.bar([i+width*2 for i in x], real_num3, alpha=0.5, width=width, label=real_names[2])
#设置x坐标的值  第1天  第2天   第3天
x_label = ['第1天', '第2天', '第3天']
plt.xticks([i+width for i in x], x_label)
plt.ylabel('票房数')
plt.legend()
plt.title('3天3部电影票房数')
plt.show()