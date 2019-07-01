#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   pa_DouBan.py
@Time    :   2019/07/01 10:13:36
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
import requests
from bs4 import BeautifulSoup
import multiprocessing as mp
mp.set_start_method('spawn', True)
import datetime

def spider(page):
    url = 'https://movie.douban.com/top250'
    header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    args = {'start' : page,'filter' : ''}
    requests.get(url,args)
    print('正在爬取', url, args)
if __name__ == '__main__':
    #计算时间
    start = datetime.datetime.now()
    pages = [i*25 for i in range(1, 10)]
    #多线程
    print('多线程')
    p = mp.Pool()
    p.map_async(spider, pages)
    p.close()
    p.join()
    end = datetime.datetime.now()
    print("last time: ", end-start)
    #单线程
    print('单线程')
    start = datetime.datetime.now()
    for i in pages:
        spider(i)
    end = datetime.datetime.now()
    print("last time: ", end-start)