# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:45:13 2020

@author: Administrator
"""

import matplotlib.pyplot as plt
#导入3D包
from mpl_toolkits.mplot3d import Axes3D

x = [1,1,2,2]
y = [3,4,4,3]
z = [1,100,1,1]
figure = plt.figure()
#创建Axes3D对象
ax = Axes3D(figure)
ax.plot_trisurf(x, y, z)
plt.show()
