# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:17:54 2020

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np

#绘制10种大小  100种颜色的散点图
np.random.seed(0)  #随机种子
x = np.random.rand(100)
y = np.random.rand(100)
#生成10种大小
size = np.random.rand(10)*1000
#生成100种颜色
color = np.random.rand(100)
#绘制散点图
plt.scatter(x, y, s=size, c=color, alpha=0.7) #s表示点的大小，c表示点的颜色，alpha表示点的透明度
plt.show()