# -*- coding: utf-8 -*-
import scrapy
from weibo.items import WeiboItem

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['weibo.cn']
    start_urls = ['https://tieba.baidu.com/f?ie=utf-8&kw=%E9%BB%91%E4%B8%9D']

    def parse(self, response):
        item = WeiboItem()
        #//div[@class='WB_text W_f14']
        #https://tieba.baidu.com/f?ie=utf-8&kw=%E9%BB%91%E4%B8%9D
        #//div[@class='threadlist_lz clearfix']//a/text()
        title_list = response.xpath("//div[@class='threadlist_lz clearfix']//a/text()").extract()
        for txt in title_list:
            item['article'] = txt
            yield item