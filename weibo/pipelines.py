# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient


class WeiboPipeline(object):

    def __init__(self):
        self.file = open("test.json","w",encoding='UTF-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item),ensure_ascii = False)+",\n"
        self.file.write(text)
        return item

    def close_spider(self):
        self.file.close()

class CommentMessPipeline(object):

    def __init__(self):
        self.file = open("lsn.json","a+",encoding='UTF-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item),ensure_ascii = False)+",\n"
        self.file.write(text)
        return item

    def close_spider(self):
        self.file.close()

class SaveMongodb_Pileline(object):

    def __init__(self):
        client = MongoClient('192.168.199.137',27017)
        db = client.weibo
        self.comment = db.comment

    def process_item(self, item, spider):
        text = dict(item)
        self.comment.insert(text)
        return item