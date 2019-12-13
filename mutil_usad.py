#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   mutil_usad.py
@Time    :   2019/12/12 15:41:32
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用多进程爬虫
'''

# here put the import lib
import multiprocessing
import requests
import os
import time
from bs4 import BeautifulSoup

def get_info(index):
    """request 请求生成器
    
    :param str url: 请求地址
    :param int index: 偏移量
    """
    for i in range(index):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
        headers = {'user-agent':user_agent} 
        url = f'https://usdawatercolors.nal.usda.gov/pom/search.xhtml?start={i*20}'
        r = requests.get(url, headers=headers)
        #休眠一秒
        time.sleep(1)
        s = BeautifulSoup(r.text)
        #文本信息
        defList = s.find_all('dl',class_='defList')
        for p in defList:
            dt = p.find_all('dt')
            dd = p.find_all('dd')
            length = len(dt)
            info = {}
            for i in range(length):
                #[-1:]删除冒号
                k = get_upper(dt[i].text[:-1])
                v = dd[i].text.replace('\n', '')
                info.setdefault(k, v)
            yield info
#utils
def get_upper(s):
    """获得大写驼峰式字符串

    param: str s: 字符串
    """
    return ''.join([i[0].upper() + i[1:] for i in s.split(' ')])
def color_print(*args):
    """彩色打印😂

    :param str s: 打印内容
    """
    print('\033[1;35m{} \033[0m'.format(args))
def export_info(fruit):
    with open('fruit.txt', 'a+') as f:
            f.write(str(fruit) + '\n')
def show_info(fruit):
    print(fruit)
if __name__ == '__main__':
    multiprocessing.set_start_method('spawn', True)
    with multiprocessing.Pool(processes=2) as pool:
        pool.map(export_info,get_info(20))