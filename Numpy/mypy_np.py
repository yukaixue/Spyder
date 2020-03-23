# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:38:54 2020

@author: Administrator
"""

#导入numpy
import numpy as np


#创建数组
a = np.arange(10)
print(a)
#对ndarray对象进行向量处理
print(np.sqrt(a))


#对列表中的元素开平方
import math
b = [i for i in range(10)]
#定义储存开平方结果的列表
result = []
#遍历列表
for i in b:
    result.append(math.sqrt(i))
print(result)  