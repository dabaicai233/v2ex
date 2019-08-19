# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from V2ex import settings


class V2ExPipeline(object):
    def __init__(self):
        self.conn = pymysql.Connect(**settings.DB_CONFIG)

    def process_item(self, item, spider):
        sql = 'INSERT INTO v2(title, text)values ( %(title)s, %(text)s)'
        with self.conn as c:

            # args可以是元组， 对应是sql语句中的 %s
            # 也可以是字典,  对应是sql语句中的 %(key)s
            c.execute(sql, args=dict(item))
        return item
