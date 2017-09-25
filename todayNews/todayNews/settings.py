# -*- coding: utf-8 -*-

# Scrapy settings for todayNews project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'todayNews'

SPIDER_MODULES = ['todayNews.spiders']
NEWSPIDER_MODULE = 'todayNews.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'todayNews (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
	'Accept':'text/javascript, text/html, application/xml, text/xml, */*',
	'Accept-Encoding':'gzip, deflate, sdch, br',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'Cache-Control':'no-cache',
	'Connection':'keep-alive',
	'Content-Type':'application/x-www-form-urlencoded',
	'Cookie':'uuid="w:3db0708ea2c549fab1a5371c56f16176"; UM_distinctid=15c7147fecd8d-0a4277451-4349052c-100200-15c7147fecf6f; csrftoken=af9a5a0d4cd30794e6c04511ca9f31eb; _ga=GA1.2.312467779.1496549163; __guid=32687416.738502311042654200.1505560389379.9048; tt_track_id=c7baa73a99ec9787ead7a2f6b01ff56b; _ba=BA0.2-20170923-51d9e-ErxmsyZIIoxNOzZgf6Us; tt_webid=6427627096743282178; WEATHER_CITY=%E5%8C%97%E4%BA%AC; CNZZDATA1259612802=610804389-1496543540-null%7C1506261975; __tasessionId=0vta7k1uc1506263833592; tt_webid=6427627096743282178',
	'Host':'www.toutiao.com',
	'Pragma':'no-cache',
	'Referer':'https://www.toutiao.com/ch/news_tech/',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
	'X-Requested-With':'XMLHttpRequest'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'todayNews.middlewares.TodaynewsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'todayNews.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {	
   'todayNews.pipelines.MongoPipeline': 300,
   'scrapy_redis.pipelines.RedisPipeline': 301
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
DOWNLOAD_DELAY = 1   
MONGO_URI=""
MONGO_DATABASE="toutiao"
MONGO_USER=""
MONGO_PASS=""
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
REDIS_URL = 'redis://usr:pwd@ip:host'
SCHEDULER_IDLE_BEFORE_CLOSE = 10