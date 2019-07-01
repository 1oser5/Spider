#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   pa_12306.py
@Time    :   2019/07/01 11:12:20
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import datetime

#寻找及输入函数
def find_enter(diver,id,text):
    it = diver.find_element_by_id(id)
    it.click()
    it.clear()
    it.send_keys(text)
    time.sleep(1)
    it.send_keys(Keys.RETURN)
def sub_date(t1):
    today = datetime.date.today()
    d = datetime.datetime.strptime(t1, '%Y-%m-%d').date()
    t = d -today
    if t.days < 0 or t.days >30:
        return False
    return t.days
def spider(from_text, to_text, date):
    #创建webdriver实例
    driver = webdriver.Chrome('/Users/xtl/Downloads/chromedriver')
    #浏览器最大化
    driver.maximize_window()
    #url
    driver.get("https://www.12306.cn/index/")
    #等待页面加载
    time.sleep(3)
    #出发地
    find_enter(driver,'fromStationText',from_text)
    #目的地
    find_enter(driver,'toStationText',to_text)
    train_date = driver.find_element_by_id('train_date')
    train_date.click()
    time.sleep(1)
    #获得相减时间
    item = sub_date(date)
    #如果有返回值
    if item:
        #获得日期数据集
        cell = driver.find_elements_by_class_name('so')
        #点击选择日期
        cell[item].click()
        search = driver.find_element_by_id('search_one')
        search.click()
    else:
        print('输入日期不符合规范或超出预约时间段')

if __name__ == '__main__':
    from_text = input('输入出发地:')
    to_text = input('输入目的地: ')
    date = input('输入日期: ')
    spider(from_text, to_text, date)
    while 1:
        pass
