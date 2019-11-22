#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   pa_weather.py
@Time    :   2019/11/22 17:26:20
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   爬取天气
'''

# here put the import lib
import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
headers = {'user-agent':user_agent}
r  = requests.get('http://www.weather.com.cn/weather1d/101210101.shtml',headers=headers)




if __name__ == '__main__':
    pass