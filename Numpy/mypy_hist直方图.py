# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:33:39 2020

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np


#生成1000个标志的正态分布随机数
x = np.random.randn(1000)
kwargs = dict(bins=100, alpha=0.4)  #bins=100   10个柱合并1个
plt.hist(x, **kwargs)   

plt.show()