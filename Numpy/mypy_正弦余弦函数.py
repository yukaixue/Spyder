# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:35:02 2020

@author: Administrator
"""

#导入matplotlib和numpy模块
from matplotlib import pyplot as plt
import numpy as np


#生成0-10之间  100个等差数
x = np.linspace(0, 10, 100)
sin_y = np.sin(x)
#进行绘制正弦函数
plt.plot(x, sin_y)
#进行绘制余弦函数
cos_y = np.cos(x)
plt.plot(x, cos_y)
#保存图片
plt.savefig('sin_cos.jpg')  #默认格式是PNG
#显示
plt.show()