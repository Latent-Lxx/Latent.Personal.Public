# -*- coding: utf-8 -*-
import scrapy

from yilongwang.headers import getAsyHeaders
import yilongwang.publicMians as pm
from yilongwang.items import Yilongwang_Comment_Item
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import  time
from bs4 import BeautifulSoup
import re
import linecache
from scrapy_redis.spiders import RedisSpider




class CommentSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['hotel.elong.com']
    start_urls=['http://hotel.elong.com/91297500/'];

    urls_list = [];
    # 最大页数
    max_page = 1

    # 请求文本的行数
    num = 20;


    def __init__(self):
        chrome_options = webdriver.ChromeOptions();
        # 浏览器隐藏模式，并不加载图片
        prefs = {'profile.managed_default_content_settings.images': 2}
        chrome_options.add_experimental_option('prefs', prefs);
        # chrome_options.add_argument('--headless');
        # chrome_options.add_argument('--disable-gpu');
        chromedriver_path = '/home/latent-lxx/下载/chromeDrive/chromedriver';

        # self.driver = webdriver.Chrome(executable_path=chromedriver_path,);
        self.driver = webdriver.Chrome(executable_path=chromedriver_path,chrome_options=chrome_options);
        super(CommentSpider,self).__init__();





    # # 循环请求文本中的网站
    # def start_requests(self):
    #             yield scrapy.Request(url='http://hotel.elong.com/wuyishan/',
    #                                  callback=self.parse,
    #                                  dont_filter='flase',
    #                                  headers=getAsyHeaders(),
    #                                  );





    # 页面跳转
    def parse(self, response):
        if(self.num < 806):
            string = linecache.getline('/home/latent-lxx/Desktop/elong/hotelUrls',self.num)
            urls = 'http://hotel.elong.com/' + re.findall('\d+',string)[0];
            yield scrapy.Request(url=urls,
                                 callback=self.parse_page,
                                 dont_filter='flase',
                                 headers=getAsyHeaders(),
                                 );
            self.num += 1;
        else:
            pm.getPrint('==> 爬去结束...','',31)

    def parse_page(self,response):
         try:
             responses = response.xpath('//*[@id="comment_paging"]/a[7]/text()')[0].extract();
             self.max_page = int(responses)
         except Exception as e:
            responses = response.xpath('//*[@id="comment_paging"]/a[8]/text()')[0].extract();
            self.max_page =int(responses)
         for i in range(self.max_page):
            time.sleep(1);
            pm.getPrint('==> 当前最大页面为：',self.max_page,31);
            try:
                next_page = self.driver.find_element_by_xpath('//*[@id="comment_paging"]/a[9]');
                ActionChains(self.driver).double_click(next_page).perform();
                self.driver.implicitly_wait(5)
                time.sleep(5);
                html1 = self.driver.page_source;
                pm.getPrint('==> 正在解析数据...', '', 32)
                item = Yilongwang_Comment_Item()
                bs = BeautifulSoup(html1, 'lxml');

                # 提取酒店名称
                name = bs.find_all("div", attrs={'class': 't24 yahei', 'title': True, })[0].text;
                item['name'] = name.replace('\n', '');

                # 提取评论
                responses = bs.find_all("p", attrs={'class': 'cmt_txt', });
                for i in responses:
                    item['comment'] = i.text;
                    yield item;
                pm.getPrint('\n页面跳转成功...', '', 32)
                pm.getPrint('\n当前项目为:', self.num, 31)

            except Exception as e:
                next_page = self.driver.find_element_by_xpath('//*[@id="comment_paging"]/a[8]');
                ActionChains(self.driver).double_click(next_page).perform();
                self.driver.implicitly_wait(5)
                time.sleep(5);
                html2 = self.driver.page_source;

                pm.getPrint('==> 正在解析数据...', '', 32)
                item = Yilongwang_Comment_Item()
                bs = BeautifulSoup(html2, 'lxml');

                # 提取酒店名称
                name = bs.find_all("div", attrs={'class': 't24 yahei', 'title': True, })[0].text;
                item['name'] = name.replace('\n', '');

                # 提取评论
                responses = bs.find_all("p", attrs={'class': 'cmt_txt', });
                for i in responses:
                    item['comment'] = i.text;
                    yield item;
                pm.getPrint('==> 页面跳转成功...', '', 32);
                pm.getPrint('\n==> 当前项目为:', self.num, 31)


            # 获取第二条链接


         string = linecache.getline('/home/latent-lxx/Desktop/elong/hotelUrls',self.num)
         urls = 'http://hotel.elong.com/' + re.findall('\d+',string)[0];
         yield scrapy.Request(url=urls,
                             callback=self.parse,
                             dont_filter='flase',
                             headers=getAsyHeaders(),
                             );




    def close(spider, response):
        spider.driver.close();







