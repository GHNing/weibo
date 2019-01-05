# -*- coding: utf-8 -*-
import scrapy
from weibo.items import CommentMess

class CommentGetSpider(scrapy.Spider):
    name = 'comment_get'
    allowed_domains = ['weibo.cn']
    start_urls = []
    custom_settings = {
        'ITEM_PIPELINES': {'weibo.pipelines.CommentMessPipeline': 300, }
    }

    def start_requests(self):
        cookie = {'_T_WM': '0756c121808bdf0dbe5b5c70543b5ba8',
                  'SCF': 'Akcn8Pka8Ccm65nuehQNFkLlhPtf5WZ4QazhcCoOP-zDUzRriDucu9IX07ZZT2-k3mPB2Y5rqg1QinqE8Lu-zH8.',
                  'SUB': '_2A25xLy_dDeRhGeBG61cV8inIzDuIHXVS07GVrDV6PUJbktAKLWbWkW1NRjxR0ikDpchA3crlv-COF80aFQWs0Qpr',
                  'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WF828oAMnlAoAF1aOjmNvaT5JpX5KzhUgL.FoqReh-XeoMXS0M2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMc1h5fShzNShMN',
                  'SUHB': '0A05aUB314TYw2'}
        start_url = 'https://weibo.cn/comment/HayiS26gh?uid=5644764907&rl=0#cmtfrm'
        yield scrapy.Request(start_url,cookies=cookie,callback=self.comment)

    def parse(self, response):
        pass
    #嵌套选择器
    def comment(self, response):
        item = CommentMess()
        comments = response.xpath("//div[@class='c']/span[@class='ctt']/text()").extract()
        for comment in comments:
            item['user_comment'] = comment
            yield item







