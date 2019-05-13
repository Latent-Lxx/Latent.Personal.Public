from yilongwang import  publicMians as PM;
import redis
from scrapy.http import HtmlResponse;
import time;
import base64
from  scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from scrapy import signals

from selenium.webdriver.common.action_chains import ActionChains


import yilongwang.publicMians as pm


"""*******状态码中间层******"""
class CodeStatusMiddleware(object):

    def process_response(self, response, request, spider):
        if response.status == 200:
            PM.getCorlor('==> <200>访问正常.','',1,40,42);
            return response
        elif response.status == 429:
            PM.getCorlor('==> <429>请求失败！','',1,40,41);
            PM.getPrint('==> 请求太过频繁！','',31);
            redisdb = redis.Redis(host='192.168.0.102', port=6379, db=0, decode_responses='true');
            redisdb.lpush('except_urls:urls',response.url)
            return response
        elif response.status == 403:
            PM.getCorlor('==> <403>请求失败！','',1,40,41);
            PM.getPrint('==> 请求被拒绝！','',31);
            return response


        elif response.status == "503 Service Unavailable":

            PM.getCorlor('==> <503>请求失败', '', 1, 40, 41);

            PM.getPrint('==> 服务器维护或容量不足！', '', 31);

            return response

        else:
            return response




"""*******页面中间层******"""
class PageMiddleware(object):

    def process_request(self,request, spider):

        try:
            pm.getPrint('==> 开启页面中间层','',32);

            # ==> 获取点评，防止加载失败:”全部“->'推荐'->'全部'
            spider.driver.get(request.url);
            spider.driver.implicitly_wait(200)
            time.sleep(1);
            # 点击点评
            dianping = spider.driver.find_element_by_xpath('//*[@id="tabMenu"]/ul/li[4]');
            ActionChains(spider.driver).double_click(dianping).perform();
            spider.driver.implicitly_wait(10)
            time.sleep(2);
            # 点击推荐
            tuijian = spider.driver.find_element_by_xpath('//*[@id="review"]/div[1]/div[2]/ul/li[2]');
            ActionChains(spider.driver).double_click(tuijian).perform();
            spider.driver.implicitly_wait(10)
            time.sleep(5);
            # 点击全部
            quanbu = spider.driver.find_element_by_xpath('//*[@id="review"]/div[1]/div[2]/ul/li[1]');
            ActionChains(spider.driver).double_click(quanbu).perform();
            spider.driver.implicitly_wait(10)
            time.sleep(2);

        except Exception as e:
            pass
        # ==> 判断是否有上一页

        # try:
        #     previous_page = spider.driver.find_element_by_xpath('//*[@id="comment_paging"]/a[1]')
        #     html = spider.driver.page_source;
        #     spider.driver.find_element_by_xpath('//*[@id="comment_paging"]/a[9]').click()
        #     time.sleep(0.3);
        #     return HtmlResponse(url=spider.driver.current_url, body=html, encoding='utf-8', request=request);
        #
        # except Exception as e:
        #     html = spider.driver.page_source;
        #     spider.driver.find_element_by_xpath('//*[@id="comment_paging"]/a[9]').click();
        #     time.sleep(0.3);
        #     return HtmlResponse(url=spider.driver.current_url, body=html, encoding='utf-8', request=request);

        html = spider.driver.page_source;


        # for i in range(99):
        #     try:
        #         next_page = spider.driver.find_element_by_xpath('//*[@id="comment_paging"]/a[9]');
        #         ActionChains(spider.driver).double_click(next_page).perform();
        #         spider.driver.implicitly_wait(1)
        #         time.sleep(1);
        #         html = spider.driver.page_source;
        #         return HtmlResponse(url=spider.driver.current_url, body=html, encoding='utf-8', request=request);
        #
        #     except :
        #         next_page = spider.driver.find_element_by_xpath('//*[@id="comment_paging"]/a[8]');
        #         spider.driver.implicitly_wait(1)
        #         ActionChains(spider.driver).double_click(next_page).perform();
        #         time.sleep(1);
        #         html = spider.driver.page_source;
        #         return HtmlResponse(url=spider.driver.current_url, body=html, encoding='utf-8', request=request);
        return HtmlResponse(url=spider.driver.current_url, body=html, encoding='utf-8', request=request);


"""*******配置阿布云******"""

class ABProxyMiddleware(HttpProxyMiddleware):

    # #==> 自己的代理
    proxyUser = "HG31GS3DS12SJ6TD"
    proxyPass = "C5E3EDFC90B3D10C"
    proxyServer = "http://http-dyn.abuyun.com:9020"


    '''======>    不加http:// 会报方案b出错的问题！            '''



    proxyAuth = 'Basic ' + base64.urlsafe_b64encode(bytes((str(proxyUser) + ':' + str(proxyPass)), 'ascii')).decode(
        'utf8')

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.
        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i
    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):

        for r in start_requests:
            yield r

    def spider_opened(self, spider):

        spider.logger.info('Spider opened: %s' % spider.name)


    def process_request(self, request, spider):

        request.meta["proxy"] = self.proxyServer

        request.headers["Proxy-Authorization"] = self.proxyAuth






