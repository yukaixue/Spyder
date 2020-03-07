# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:05:09 2020

@author: Administrator
"""



from selenium import webdriver
from selenium.webdriver.common.by import By #用于指定 HTML 文件中 DOM 标签元素
from selenium.webdriver.support.ui import WebDriverWait #等待网页加载完成
from selenium.webdriver.support import expected_conditions as EC #指定等待网页加载结束条件






def get_music_name():
    url = 'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w={}'.format('告白气球')
    
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(5)
    data = driver.find_element_by_xpath('//*[@id="song_box"]/div[2]/ul[2]/li[1]/div/div[2]/a').get_attribute('href')
    
    print(data)
get_music_name()



