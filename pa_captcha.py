#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   WorkCap.py
@Time    :   2019/06/27 10:21:12
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
import time
url = 'https://captcha.com/captcha-examples.html?cst=corg'

#路由
result = []
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
r = requests.get(url, headers = header)
soup = BeautifulSoup(r.text)
img = soup.find_all('img',class_ = 'captcha_sample')
folder_path = './photo/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)  # 创建文件夹
# for i in img:
#     img_name = folder_path + str(i + 1) +'.png'
#     with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
#         file.write(html.content)
#         file.flush()
#     file.close()  # 关闭文件
#     print('第%d张图片下载完成' %(i+1))
#     time.sleep(1)  # 自定义延时
# print(result)
for index,item in enumerate(img):
    html = requests.get('https://captcha.com/' + item.get('src'))
    img_name = folder_path + str(index + 1) +'.png'
    with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
        file.write(html.content)
        file.flush()
    file.close()  # 关闭文件
    print('第%d张图片下载完成' %(index+1))
    time.sleep(1)  # 自定义延时
print('抓取完成')
