# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:20:35 2020

@author: Administrator
"""

import matplotlib.pyplot as plt


#200个点的坐标
x = range(-100, 100)
#生成y点的坐标
y = [i**2 for i in x]
#绘制一元二次曲线
plt.plot(x, y)
plt.rcParams['axes.unicode_minus']=False  #用来正常显示负号
#保存图片
plt.savefig('result.jpg')  #默认格式是PNG
#显示
plt.show()