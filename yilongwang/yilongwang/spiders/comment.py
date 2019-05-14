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
import os





class CommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['hotel.elong.com']
    start_urls=['http://hotel.elong.com/92483891/'];

    # 把文本每一行的url装到list中
    urls_list = [];
    # 最大页数
    max_page = 1
    # 请求文本的行数
    num = 46;

    # 获取当前文件父路径
    feather_path = os.getcwd();


    def __init__(self):
        chrome_options = webdriver.ChromeOptions();
        # 浏览器隐藏模式，并不加载图片
        prefs = {'profile.managed_default_content_settings.images': 2}
        chrome_options.add_experimental_option('prefs', prefs);
        # 如果自动运行中评论内容没有变化，需要注释这儿
        chrome_options.add_argument('--headless');
        # chrome_options.add_argument('--disable-gpu');
        chromedriver_path = f'{self.feather_path}/yilongwang/elong/chromedriver';
        self.driver = webdriver.Chrome(executable_path=chromedriver_path,chrome_options=chrome_options);
        super(CommentSpider,self).__init__();




    # 页面跳转
    def parse(self, response):
        # 最多不超过806行
        if(self.num < 806):
            string = linecache.getline(f'{self.feather_path}/yilongwang/elong/hotelUrls',self.num)
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

         # 获取每个项目最大的页数
         try:
             responses = response.xpath('//*[@id="comment_paging"]/a[7]/text()')[0].extract();
             self.max_page = int(responses)
         except Exception as e:
            #  如果获取页数失败
            try:
                responses = response.xpath('//*[@id="comment_paging"]/a[8]/text()')[0].extract();
                self.max_page =int(responses);
            except Exception as e :
                self.num += 1;
                string = linecache.getline(f'{self.feather_path}/yilongwang/elong/hotelUrls', self.num)
                urls = 'http://hotel.elong.com/' + re.findall('\d+', string)[0];
                yield scrapy.Request(url=urls,
                                     callback=self.parse,
                                     dont_filter='flase',
                                     headers=getAsyHeaders(),
                                     );

         # 循环爬取页面，并点击下一页，
         '''
         rangge中的数字10，表示只爬取每个项目的前10页，如果写成self.max_page,则会爬取每个酒店所有的页面
         '''
         for i in range(10):
            time.sleep(1.5);

            pm.getPrint('==> 当前最大页面为：',self.max_page,31);

            # 点击下一页，验证是否是第一页，第一页的下一页和第二页的下一页，他们的元素位置不同。
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


         string = linecache.getline(f'{self.feather_path}/yilongwang/elong/hotelUrls',self.num)
         urls = 'http://hotel.elong.com/' + re.findall('\d+',string)[0];
         yield scrapy.Request(url=urls,
                             callback=self.parse,
                             dont_filter='flase',
                             headers=getAsyHeaders(),
                             );




    def close(spider, response):
        spider.driver.close();







