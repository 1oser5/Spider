#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   pa_zhihu.py
@Time    :   2019/06/29 10:05:19
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#创建浏览器实例
driver = webdriver.Chrome()

url = 'https://www.zhihu.com/'
cookie = '''_zap=e31c4ff4-6c04-4780-bced-3cc059a9a688; d_c0="AIBk1TFDPw6PTtyRcH6fQs8ymy8F-3JNWgk=|1537543641"; _xsrf=njl3vNg6kMAe2mlvez3QPN2N2iFfW2vm; __utma=155987696.732252355.1542531785.1542531785.1542531785.1; q_c1=9003016b241c41bcaa4d90626cbbeaf5|1556435386000|1537543643000; tgw_l7_route=4860b599c6644634a0abcd4d10d37251; capsion_ticket="2|1:0|10:1561773649|14:capsion_ticket|44:MmE4YTNjZDljMTMzNDNhOGIyNDEwYzUxNjg5YWRkZjI=|981ce888bf23095d69e2ac81937691635aee94b2f19cdf7cf0fd9141fe533483"; z_c0="2|1:0|10:1561773681|4:z_c0|92:Mi4xV19LbUF3QUFBQUFBZ0dUVk1VTV9EaVlBQUFCZ0FsVk5jQlFFWGdCTUhfd1ZuNHktWUx4akNHMnZDSTYyS1AycVV3|a74c264eb0f0384e470a3a19f93c9ff3f5e57c2179180793da39fdd1cb525665"; unlock_ticket="ABBARamwywomAAAAYAJVTXjNFl2InDia08-nvg6iKtwp_fOh02xgIQ=="; tst=r'''
header = {    
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',    
'Connection': 'keep-alive',       
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',  
'Cookie': cookie
}

r = requests.get(url, headers = header)
print(r.cookies)
soup = BeautifulSoup(r.text)
print(soup)
