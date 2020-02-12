# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:10:27 2020

@author: Administrator
"""

het,wet = eval(input('请输入身高(米)和体重(公斤)[逗号隔开]：'))
bmi = wet/pow(het,2)
print('BMI 指数为：{:.2f}'.format(bmi))
who = ''
if bmi <18.5:
    who = '偏瘦'
elif 18.5 <= bmi <25:
    who = '正常'
elif 25 <= bmi <30:
    who = '偏胖'
else:
    who = '肥胖'
print("BMI 指标为：国际{}".format(who))