# -*- coding: utf-8 -*-
import scrapy
from weibo.items import WeiboItem

class CookieSpider(scrapy.Spider):
    name = 'cookie'
    allowed_domains = ['weibo.cn']
    start_urls = ['http://weibo.cn/']

    def parse(self, response):
        url = "https://weibo.cn/?tf=5_009"
        '''
        cookie = {
            '_T_WM': 'a9f9dbc4e99ab7d9b3fe18f59ae3c32e',
            'SUB': '_2A25xLKJqDeRhGeBH6lIV8SvJwj-IHXVS7s4irDV6PUJbkdAKLWrdkW1NQcO2dWpE6upA-gVsIv8mo4hH3zxi5vsv',
            'gsid_CTandWM': '4uru3eaa16sZIj9z'
        }
        '''
        cookie = {'_T_WM': '430b6c7ad739b2b6ce9b9588a0dafd62',
               'SCF': 'Akcn8Pka8Ccm65nuehQNFkLlhPtf5WZ4QazhcCoOP-zDNC-DYAZdq259dPOsI8SAbnJn22NgzzD0xRCGPI7QcWU.',
               '__guid': '78840338.3451898839486744600.1546183169101.0398',
               'SUB': '_2A25xLyoVDeRhGeBH6lIV8SvJwj-IHXVS07ZdrDV6PUJbkdAKLRnckW1NQcO2dTXdWgBc0rHrnbAvXdk-1-uf9TXi',
               'SUHB': '0JvgaVkKIbqEtP', 'SSOLoginState': '1546345029', 'monitor_count': '3'}

        yield scrapy.Request(url,cookies=cookie,callback=self.custom_cookie)

    def custom_cookie(self,response):
        item = WeiboItem()
        #item['article'] =response.xpath("//div[@class='ut']/text()").extract()[0]

        context_list = response.xpath("//div[@class='c']//span[@class = 'ctt']/text()").extract()
        for i in context_list:
            item['article'] = i
            yield item


