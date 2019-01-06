# -*- coding: utf-8 -*-
import scrapy
from weibo.items import CommentMess
import math

class CommentGetSpider(scrapy.Spider):
    name = 'comment_get'
    allowed_domains = ['weibo.cn']
    start_urls = []
    custom_settings = {
        'ITEM_PIPELINES': {'weibo.pipelines.CommentMessPipeline': 300, }
    }
    _cookie = {'_T_WM': '0756c121808bdf0dbe5b5c70543b5ba8',
              'SCF': 'Akcn8Pka8Ccm65nuehQNFkLlhPtf5WZ4QazhcCoOP-zDUzRriDucu9IX07ZZT2-k3mPB2Y5rqg1QinqE8Lu-zH8.',
              'SUB': '_2A25xLy_dDeRhGeBG61cV8inIzDuIHXVS07GVrDV6PUJbktAKLWbWkW1NRjxR0ikDpchA3crlv-COF80aFQWs0Qpr',
              'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WF828oAMnlAoAF1aOjmNvaT5JpX5KzhUgL.FoqReh-XeoMXS0M2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMc1h5fShzNShMN',
              'SUHB': '0A05aUB314TYw2'}

    def __init__(self):
        self.item = CommentMess()

    def start_requests(self):
        #start_url = 'https://weibo.cn/comment/HayiS26gh?uid=5644764907&rl=0#cmtfrm'
        start_url = 'https://weibo.cn/comment/H9KAejNLi?uid=6179279336&rl=0#cmtfrm'
        yield scrapy.Request(start_url,cookies=self._cookie,callback=self.page_deal)

    def parse(self, response):
        pass


    def page_deal(self, response):
        count = response.xpath("//div/span[@class='pms']/text()").extract()[0]
        page_count = math.ceil(int(count.strip()[3:-1])/10)
        for i in range(int(page_count)):
            page_url = "https://weibo.cn/comment/H9KAejNLi?uid=6179279336&rl=0&page=" + str(i+1)
            yield scrapy.Request(page_url,cookies=self._cookie,callback=self.comment)


    def comment(self, response):
        xml_list = response.xpath("//div[@class='c']")
        basic_url = "https://weibo.cn"
        #处理xml
        for xml in xml_list:
            try:
                if xml.xpath("@id").extract() and xml.xpath("./a"):
                    if not xml.xpath("./span[@class='kt']"):
                        self.item['user_name'] = xml.xpath("./a[1]/text()").extract()[0]
                        self.item['user_url'] = basic_url + xml.xpath("./a[1]/@href").extract()[0]
                        self.item['user_comment'] = xml.xpath("./span[@class='ctt']/text()").extract()[0]
                        yield self.item
            except :
                continue











