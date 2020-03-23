# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:57:21 2020

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
#使用legend()添加图例，给iplot方法添加参数label
plt.plot(x, x+0, '--g', label='1')
plt.plot(x, x+1, '-.r', label='2')
plt.plot(x, x+2, ':b', label='3')
plt.plot(x, x+3, '.k', label='4')
plt.plot(x, x+4, ',c', label='5')
plt.plot(x, x+5, '*y', label='6')
#左上角upper left             fancybox边框   framealpha透明度 shadow阴影  borderpad边框宽度
plt.legend(loc='lower right', fancybox=True, framealpha=0.5, shadow=True, borderpad=1)  #默认在左上角
plt.show()