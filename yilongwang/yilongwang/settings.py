# -*- coding: utf-8 -*-

# Scrapy settings for yilongwang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html


from mock_useragent import MockUserAgent


BOT_NAME = 'yilongwang'

SPIDER_MODULES = ['yilongwang.spiders']
NEWSPIDER_MODULE = 'yilongwang.spiders'



#==> 配置User-Agent
ua = MockUserAgent()
USieER_AGENT =ua.random_chrome



#==> 配置redis

# REDIS_URL = 'redis://127.0.0.1:6379/0'

#启用Redis调度存储请求队列
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#
# #确保所有的爬虫通过Redis去重
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#
# #不清除Redis队列、这样可以暂停/恢复 爬取
# SCHEDULER_PERSIST = 'true'
#
# # #使用优先级调度请求队列 （默认使用）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
#
# # 关掉一个scrapy shell
# EXTENSIONS = {
#     'scrapy.telnet.TelnetConsole': None
#  }
#





# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'chinese_goods (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 16

# Co/
DOWNLOAD_DELAY = 1


# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 64
# CONCURRENT_REQUESTS_PER_IP = 64

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'chinese_goods.middlewares.ChineseGoodsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
     'yilongwang.middlewares.CodeStatusMiddleware':1,
     'yilongwang.middlewares.PageMiddleware':1,
     # 'yilongwang.middlewares.ABProxyMiddleware':1,

}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'yilongwang.pipelines.YilongwangPipeline': 100,
   # 'scrapy_redis.pipelines.RedisPipeline': 100,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = 'true'
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = 'true'
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#
# REDIRECT_ENABLED = False
# allow_redirects='true'
# DOWNLOAD_TIMEOUT = 300
# SPEED_INDEX_RULE_LAST=1
# SPEED_INDEX_HIGHER_PRIORITY=1
# REACTOR_THREADPOOL_MAXSIZE = 1000


