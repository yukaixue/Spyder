# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:51:21 2020

@author: Administrator
"""

import matplotlib.pyplot as plt


#准备绘制的两个点
x = [1,2,3,4,5]
y = [1,4,9,16,25]

#调用绘制plot方法
#linewidth属性设置线条的宽度
plt.plot(x, y, linewidth=5)
#添加x,y轴的名称
plt.xlabel('x')
plt.ylabel('y=x^2')
plt.rcParams['font.sans-serif']=['SimHei']#用来正常显示中文标签
#给图标添加标题
plt.title('多个点绘制折线图')
#显示绘制的图
plt.show()