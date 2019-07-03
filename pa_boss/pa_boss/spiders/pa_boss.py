#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   pa_boss.py
@Time    :   2019/07/02 19:57:47
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
import scrapy
import csv
import os

class boss(scrapy.Spider): #继承scray.spider类
    name = 'boss_spider' #定义蜘蛛名
    def start_requests(self):
        #url
        url = 'https://www.zhipin.com/job_detail/?query=%E7%88%AC%E8%99%AB%E5%B7%A5%E7%A8%8B%E5%B8%88&city=101210100&industry=&position='
        
        yield scrapy.Request(url = url, callback = self.parse)#使用parse方法处理回调
    
    def parse(self, response):
        #job名
        job = response.css('.info-primary .job-title::text').extract()
        #月薪
        money = response.css('.info-primary .red::text').extract()
        #工作地点
        work_place = response.css('.info-primary p::text').extract()
        work_result = [' '.join(work_place[i:i+3]) for i in range(0, len(work_place), 3)]
        #公司名称
        company = response.css('.info-company .name a::text').extract()
        
        
        #公司概述
        company_info = response.css('.info-company p::text').extract()
        company_result = [' '.join(company_info[i:i+3]) for i in range(0, len(company_info), 3)]
        #发布人名及职位
        publis_info= response.css('.info-publis h3::text').extract()
        publis_result = [' '.join(publis_info[i:i+2]) for i in range(0, len(publis_info), 2)]
       
        # 下一页
        next_page = response.css('.next::attr(href)').extract_first()
        # print(next_page)
        if next_page is not None: 
            next_page = response.urljoin('https://www.zhipin.com/'+next_page)
            yield scrapy.Request(next_page, callback=self.parse)
       
        # if not os.path.exists('test.csv'):
            with open("test.csv","w") as csvfile: 
                writer = csv.writer(csvfile)
                #先写入columns_name
                writer.writerow(["job","money","work_result","company","company_result","publis_result"])
                #写入多行用writerow
                for i in range(len(job)):
                    writer.writerow([job[i], money[i], work_result[i], company[i], company_result[i], publis_result[i]])


            
