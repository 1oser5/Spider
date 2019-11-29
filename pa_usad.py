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
import smtplib
from email.mime.text import MIMEText
import datetime
import sys
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
        self.info = args
    def download_img(self,dir_url):
        """下载高清图片
        
        :param str dir_url: 图片存储文件夹
        """
        #检查文件夹
        check_dir(dir_url)
        #timeout 参数为元组时，第一个表示 Connect 时间，第二个为 read 时间
        resp = requests.get(self.info['ImgUrl'], timeout=(3, 30))
        color_print('开始下载图片...', self.info['ImgUrl'])
        # 图片一定要以 wb (二进制)打开,文件储存为 Scientific.png 格式
        with open('{0}/{1}.png'.format(dir_url,self.info['Code']), 'wb') as f:
            f.write(resp.content)
            color_print('saved...{0}.png'.format(self.info['ImgUrl']))
    def export_info(self,info):
        """导出水果信息"""
        with open('fruit.txt', 'a+') as f:
            f.write(str(info) + '\n')
def get_high_img(code):
        """拼接高清图片"""
        return 'https://usdawatercolors.nal.usda.gov/pom/download.xhtml?id={0}'.format(code)
def check_dir(dir_url):
    """检查文件夹是否存在，如果不存在则创建

    :param str dir_url: 文件夹路径
    """
    if not os.path.exists(dir_url):
        os.makedirs(dir_url)
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
        r = requests.get(url.format(20 * i), headers=headers)
        #休眠一秒
        time.sleep(1)
        s = BeautifulSoup(r.text)
        #文本信息
        defList = s.find_all('dl',class_='defList')
        for p in defList:
            dt = p.find_all('dt')
            dd = p.find_all('dd')
            #图片编码
            Code = p.find('img')['src'].split('/')[2]
            length = len(dt)
            info = {}
            for i in range(length):
                #[-1:]删除冒号
                k = dt[i].text[:-1].get_upper()
                v = dd[i].text.replace('\n', '')
                info[k] = v
            #添加图片编码和图片url
            info['Code'] = Code
            info['ImgUrl'] = get_high_img(Code)
            #新建实例
            fruit = Fruit(info)
            #下载图片
            fruit.download_img(dir_url)
            #导出信息
            fruit.export_info(info)
def get_upper(s):
    """获得大写驼峰式字符串

    param: str s: 字符串
    """
    return ''.join([i[0].upper() + i[1:] for i in s.split(' ')])
def send_msg(use_time):
    """发送爬取结束信息

    :param int use_time : 使用时间
    """
    #设置服务器所需信息
    #163邮箱服务器地址
    mail_host = 'smtp.163.com'  
    #163用户名,用户名还不能乱写。。
    mail_user = 'snoopy98'  
    #密码(部分邮箱为授权码) 
    mail_pass = 'xxx'   
    #邮件发送方邮箱地址
    sender = 'snoopy98@163.com'  
    #邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['lzj7892@dingtalk.com']  
    #设置email信息
    content = '''
    爬取美国农业部高清图片完成
    共耗时 {} 
    '''.format(use_time)
    #邮件内容设置
    message = MIMEText(content,'plain','utf-8')
    #邮件主题       
    message['Subject'] = '爬虫' 
    #发送方信息
    message['From'] = sender 
    #接受方信息     
    message['To'] = ';'.join(receivers)
    #登录并发送邮件
    try:
        smtpObj = smtplib.SMTP() 
        #连接到服务器
        smtpObj.connect(mail_host,25)
        #登录到服务器
        smtpObj.login(mail_user,mail_pass) 
        #发送
        smtpObj.sendmail(
            sender,receivers,message.as_string()) 
        #退出
        smtpObj.quit() 
    except smtplib.SMTPException as e:
        print('error',e) #打印错误
def count_time(cls):
    """计算函数执行时间装饰器，

    param: function cls: 目标函数
    """
    def wrapper(*args, **kwargs):
        starttime = datetime.datetime.now()
        cls(*args, **kwargs)
        endtime = datetime.datetime.now()
        int_seconds = int((endtime - starttime).total_seconds())
        return format_seconds(int_seconds)
    return wrapper
def format_seconds(seconds):
    """格式化秒，返回 HH:MM:SS 格式时间
    
    param: int seconds: 秒
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return("%d:%02d:%02d" % (h, m, s))
@count_time
def main():
    #不做参数捕捉了
    dir_url = sys.argv[1:][0]
    url,headers = config()
    get_url(url, headers, dir_url, 380)
if __name__ == '__main__':
    #pylint 问题，可以正常运行
    use_time = main()
    send_msg(use_time)




