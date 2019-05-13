# -*- coding: utf-8 -*-
import scrapy
from yilongwang.headers import getAsyHeaders
from yilongwang.formDatas import getAsyFormDatas
import yilongwang.publicMians as pm
from yilongwang.items import Yilongwang_List_Item
import json

class ListSpider(scrapy.Spider):

    name = 'list'
    allowed_domains = ['hotel.elong.com']

    # 起始链接
    begin_urls = 'http://hotel.elong.com/ajax/tmapilist/asyncsearch/'

    # page

    page = 1;

    # 爬虫入口
    def start_requests(self):
        yield scrapy.FormRequest(
            url=self.begin_urls,
            headers=getAsyHeaders(),
            formdata=getAsyFormDatas(),
            dont_filter='ture',
            callback=self.parse)


    # 解析入口网页
    def parse(self, response):
        # 初始page
        if( self.page < 43):
            pm.getPrint('当前页面：',self.page, 31);
            item = Yilongwang_List_Item();
            # 格式化Json
            json_responses = json.loads(response.body_as_unicode());

            responses = json_responses['value']['hotelIds'];
            responses = responses.split(',');

            for i in responses:
                item['projectId'] = i;
                yield item


            # 跳转
            page_formdata = getAsyFormDatas();
            self.page +=1;
            page_formdata['listRequest.pageIndex'] =str(self.page)

            yield scrapy.FormRequest(
                url=self.begin_urls,
                headers=getAsyHeaders(),
                formdata=page_formdata,
                dont_filter='ture',
                callback=self.parse)

        else:
            pm.getPrint('==> 爬虫完毕！','',31)




