#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   pa_wyNews.py
@Time    :   2019/06/28 09:29:50
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
import requests
from bs4 import BeautifulSoup
import os


url = 'http://news.163.com/rank/'
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

myPage = requests.get(url,headers = header)
#需要转换编码，理由是常规编码时bs4遇到!<>类似的注释会出现未知错误，导致爬取网页结构不全
soup = BeautifulSoup(myPage.text,'html5lib')
#获得新闻div
div = soup.find_all('div', class_ = "tabContents active")
#获得标题div
title = soup.find_all('div', class_ = 'titleBar')
#文件夹生成
folder_path = './WYnews/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)  # 创建文件夹

for i,t in zip(div,title):
    a = i.find_all('a')
    with open(folder_path+t.h2.string+'.txt', 'w') as file:  # 以byte形式将图片数据写入
        for s in a:
            file.write(s.string)
            #换行
            file.write(s['href']+'\n')
        file.flush()
    file.close()  # 关闭文件

