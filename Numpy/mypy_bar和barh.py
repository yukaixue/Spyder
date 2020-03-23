# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:36:08 2020

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np

#生成x, y
np.random.seed(0)
x = np.arange(5)
y = np.random.randint(-5, 5, 5)
#将画布分为1行2列  在第一个区域画bar
plt.subplot(1, 2, 1)
#添加颜色
v_bar = plt.bar(x, y, color='blue')
#在0水平位置添加蓝色线条
plt.axhline(0, color='blue', linewidth=1)
#对y值大于0设置为蓝色，小于0的柱设置为绿色
for bar, height in zip(v_bar, y):
    if height < 0:
        bar.set(color='green')
#在第二个区域画barh
plt.subplot(1, 2, 2)
plt.barh(x, y, color='red')
#在0位置垂直方向添加红色线条
plt.axvline(0, color='red', linewidth=1)

plt.show()