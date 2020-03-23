# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:57:36 2020

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np
 
 
x = np.linspace(0, 10, 100)
sin_y = np.sin(x)
#绘制正弦的曲线
plt.subplot(2, 2, 1)
plt.plot(x, sin_y)
plt.subplot(2, 2, 2)
plt.plot(x, sin_y, 'o')  #plot速度比scatter快，第三个参数是显示符号
#绘制散点图
plt.subplot(2, 2, 3)
plt.scatter(x, sin_y)
plt.show()

'''
从上面的实例来看，使用plot绘制和使用scatter绘制出来的图形是没有区别的，但是使用plot
绘制图形的速度大于scatter，所以画一堆点，而且点的形式没有差别，那么我们使用plot，
如果点的形式有差别（点的大小和颜色不同）则必须使用scatter
'''