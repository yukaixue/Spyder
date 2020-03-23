# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:12:44 2020

@author: Administrator
"""

import matplotlib.pyplot as plt


#创建x, y  x表示年份， y表示年份对应的销量
x = [1980, 1985, 1990, 1995]
x_label=['1980年','1985年','1990年','1995年']
y = [1000, 2000, 3000, 4000]
#调用bar函数绘制柱状图
v_bar = plt.bar(x, y, width=3)   #width修改柱的宽度
#修改x坐标的值
plt.xticks(x, x_label)
#给x坐标y坐标添加名称
for bar, x in zip(v_bar, x_label):
    if x == '1990年':
        bar.set(color='red')
plt.xlabel('年份')
plt.ylabel('销量')
plt.title('根据年份销量对比图')
plt.show()