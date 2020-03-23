# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:41:28 2020

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np


# 创建0-10中100个等差数
x = np.linspace(0, 10, 100)
sin_y = np.sin(x)
#绘制正弦曲线
#对画布进行分区，将画布分为2行2列， 画到区1
plt.subplot(2, 2, 1)
#修改x, y轴的坐标范围
plt.xlim(-5, 20)
plt.ylim(-2, 2)
plt.plot(x, sin_y)


#绘制余弦曲线
cos_y = np.cos(x)
plt.subplot(2, 2, 4)
plt.xlim(0, 10)
plt.ylim(-1, 1)
plt.plot(x, cos_y)
#保存图片
plt.savefig('sin_cos_分区')  #默认格式是PNG
#显示
plt.show()