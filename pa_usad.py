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
import os
def config():
    """爬虫配置"""
    #设置头部
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    headers = {'user-agent':user_agent}
    url = 'https://usdawatercolors.nal.usda.gov/pom/search.xhtml?start={}'
    return (url,headers)
class Fruit(object):
    """水果类"""
    def __init__(self,args):
        self.Artist = args['Artist']
        self.Year = args['Year']
        self.Scientific = args['Scientific']
        self.Common = args['Common']
        self.Country = args['Country']
        self.Specimen = args['Specimen']
        self.Code = args['Code']
        self.ImgUrl = self.get_high_img()
    def get_high_img(self):
        """拼接高清图片"""
        return 'https://usdawatercolors.nal.usda.gov/pom/download.xhtml?id={0}'.format(self.Code)
    def download_img(self,dir_url):
        """下载高清图片
        
        :param str dir_url: 图片存储文件夹
        """
        #检查文件夹
        check_dir(dir_url)
        resp = requests.get(self.ImgUrl)
        # 图片一定要以 wb (二进制)打开,文件储存为 Scientific.png 格式
        with open('{0}/{1}.png'.format(dir_url, self.Scientific.replace(' ','-')), 'wb') as f:
            f.write(resp.content)
            color_print('saved...',self.Scientific.replace(' ','-'))
def check_dir(dir_url):
    """检查文件夹是否存在，如果不存在则创建

    :param str dir_url: 文件夹路径
    """
    if not os.path.exists(dir_url):
        os.makedirs(dir_url)
        color_print('build {0} successfully'.format(dir_url))
def color_print(*args):
    """彩色打印😂

    :param str s: 打印内容
    """
    print('\033[1;35m{} \033[0m'.format(args))
def get_url(url, headers, dir_url, index = 1):
    """request 请求
    
    :param str url: 请求地址
    :param dict headers: 请求头
    :param str dir_url: 存放文件路径,如果不存在默认创建
    :param int index: 循环次数
    """
    for i in range(index):
        r = requests.get(url.format(20 * i), headers = headers)
        #休眠一秒
        time.sleep(1)
        s = BeautifulSoup(r.text)
        #文本信息
        defList = s.find_all('dl',class_ = 'defList')
        for p in defList:
            c1 = p.find('dd', class_='blacklight-name_facet')
            c2 = p.find('dd',class_='blacklight-specimen_identifier_s')
            c3 = p.find_all('dd',class_='blacklight-year_facet')
            #作者
            Artist = c1.text
            #物种编号
            Specimen = c2.text
            #时间
            Year = c3[0].text
            #科学名
            Scientific = c3[1].text
            #俗名
            Common = c3[2].text
            #地区
            Country = c3[3].text if len(c3) == 4 else ''
            #图片编码
            Code = p.find('img')['src'].split('/')[2]
            info = {
                'Artist':Artist,
                'Year':Year,
                'Specimen':Specimen,
                'Scientific':Scientific,
                'Common':Common,
                'Country':Country,
                'Code':Code
                }
            #处理换行符
            for k in info:
                info[k] = info[k].replace('\n', '')
            #新建实例
            fruit = Fruit(info)
            color_print('开始下载图片...',fruit.ImgUrl)
            #下载图片
            fruit.download_img(dir_url)
if __name__ == '__main__':
    url,headers = config()
    dir_url = input('请输入文件存储文件夹\n')
    get_url(url, headers, dir_url,380)



