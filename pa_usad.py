#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   pa_usad.py
@Time    :   2019/11/27 19:10:41
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   爬取美国农业部高清图片
'''
# here put the import lib
import requests
from bs4 import BeautifulSoup
import time
#设置头部
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
headers = {'user-agent':user_agent}
#数据循环爬取
#一共380页，但是最后一样质量很低，数量也不对，暂不取
# for a in range(380):
# r = requests.get('https://usdawatercolors.nal.usda.gov/pom/search.xhtml?start={0}'.format(20 * a))
r = requests.get('https://usdawatercolors.nal.usda.gov/pom/search.xhtml?start=0', headers=headers)
#休眠一秒
time.sleep(2)
s = BeautifulSoup(r.text)
#文本信息
defList = s.find_all('dl',class_ = 'defList')
#图片
imgs = s.find_all('div',class_ = 'thumb-frame')
Artist = []
Year = []
Scientific = []
Common = []
Country = []
Specimen = []
high_img = []
for p in defList:
    #作者
    c1 = p.find('dd', class_='blacklight-name_facet')
    Artist.append(c1.text.replace("\n", ""))
    #物种编号
    c2 = p.find('dd',class_='blacklight-specimen_identifier_s')
    Specimen.append(c2.text.replace("\n", ""))
    #科学名，俗名，地区
    c3 = p.find_all('dd',class_='blacklight-year_facet')
    Year.append(c3[0].text.replace("\n", ""))
    Scientific.append(c3[1].text.replace("\n", ""))
    Common.append(c3[2].text.replace("\n", ""))
    Country.append(c3[3].text.replace("\n", "") if len(c3) == 4 else '')
for x in imgs:
    #高清图地址
    high_img.append('https://usdawatercolors.nal.usda.gov/pom/download.xhtml?id={0}'.format(x.find('img')['src'].split('/')[2]))
def download_img(ori_img_url,filename):
    resp = requests.get(ori_img_url)
    with open('/Users/xtl/Desktop/test/' + filename, 'w+') as f:
        f.write(resp.content)
        print('saved...', filename)
# for i in range(20):
download_img(high_img[0], Scientific[0])

