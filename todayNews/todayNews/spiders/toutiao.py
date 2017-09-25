# -*- coding: utf-8 -*-
from scrapy import Spider,Request
import json
import logging
from todayNews.items import TodaynewsItem
class ToutiaoSpider(Spider):
    name = "toutiao"
    allowed_domains = ["www.toutiao.com"]
    start_urls = ['https://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A1D5394CB72C38F&cp=59C71C03883F0E1']
    url='https://www.toutiao.com/api/pc/feed/?category=news_tech&utm_source=toutiao&widen=1&max_behot_time={behot_time}&max_behot_time_tmp={behot_time_tmp}&tadrequire=true&as=A165E92C97CC487&cp=59C74CC4E8F7BE1'
    def parse(self, response):
    	jsonData=json.loads(response.body.decode("utf-8"))
    	MainData=jsonData["data"]
    	nextTime=jsonData["next"]["max_behot_time"]
    	if jsonData["message"]=='success':
    		for rowData in MainData[1:]:
    			yield rowData
    		yield Request(url=self.url.format(behot_time=nextTime,behot_time_tmp=nextTime),callback=self.parse)
    	else:
    		logging.info("The Data is null")
        
