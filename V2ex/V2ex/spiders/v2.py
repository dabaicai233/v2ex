# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request



class V2Spider(scrapy.Spider):
    name = 'v2'
    allowed_domains = ['www.v2ex.com']
    start_urls = ['https://www.v2ex.com/?tab=hot']

    def parse(self, response):
        item = {}
        number = 0
        nodes = response.css('.item_title')
        for node in nodes:
            item['url_info'] = "https://www.v2ex.com/" + node.xpath('./a/@href').get()
            if number == 5:
                return
            number += 1

            yield Request(item['url_info'], self.parse1, priority=10)


    def parse1(self, response):
        item = {}
        item['title'] = response.css('h1').xpath('./text()').get()
        item['text'] = ''.join(response.css('.topic_content').xpath('.//text()').extract())
        # item['num'] = ''.join(response.css('.cell .gray').xpath('.//text()').extract_first()).replace(' 回复 \xa0','')
        yield item
