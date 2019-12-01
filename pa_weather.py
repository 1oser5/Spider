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
import smtplib
from email.mime.text import MIMEText
import datetime
import traceback
def get_weather():
    '''获取天气'''
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    headers = {'user-agent':user_agent}
    r  = requests.get('https://tianqi.911cha.com/hangzhou/',headers=headers)
    s = BeautifulSoup(r.text)
    #获取当天时间
    today = get_time()
    #获得当天天气总览
    t_weather = s.find('a',href = './{0}.html'.format(today))
    #最低温度
    min_tem = t_weather.find('span','f16').text[1:]
    #最高温度
    max_tem = t_weather.find('span','f24').text
    #日期
    date= t_weather.find('div','f12 pt').text
    #天气情况
    weather= t_weather.find('div','w_week_desc').text
    return (date,max_tem,min_tem,weather)

def get_time():
    """获得网站格式时间
    
    #原网站个位数日期的时候，显示为 2019-12-1，但 today 显示为 2019-12-01，需要移除0
    rtype: str
    """
    today = str(datetime.date.today()).split('-')
    return '-'.join([i[1:] if i[0] == '0' else i for i in today])
def send_msg(content):
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
    content = content
    #邮件内容设置
    message = MIMEText(content,'plain','utf-8')
    #邮件主题       
    message['Subject'] = '今日天气' 
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
        print('success send eamil to %s'%receivers)
    except smtplib.SMTPException as e:
        print('error',e) #打印错误

if __name__ == '__main__':
    try:
        w = get_weather()
        content = '''
    {0}
    最高温度: {1}
    最低温度: {2}
    天气情况: {3}
    '''.format(w[0],w[1],w[2],w[3])
        send_msg(content)
    except Exception as e:
        send_msg(traceback.format_exc())