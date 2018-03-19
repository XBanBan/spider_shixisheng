# -*- coding: utf-8 -*-
import scrapy
import os
from ShiXi.items import ShixiItem
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class ShixiSpider(scrapy.Spider):
    name = 'shixi'
    allowed_domains = ['shixiseng.com']
    start_urls = ['https://www.shixiseng.com/']

    def parse(self, response):
        items = []
        post = response.xpath("//div[1]/div[4]/div/div[1]//a/text()").extract()
        urls = response.xpath("//div[1]/div[4]/div/div[1]//a/@href").extract()

        for i in range(0, len(post)):
            filename = "./Data/" + post[i]
            url = 'https://www.shixiseng.com' + urls[i]
            if(not os.path.exists(filename)):
                os.makedirs(filename)
            item = ShixiItem()
            item['filename'] = filename
            item['post'] = post[i]
            item['urls'] = url
            items.append(item)
        for item in items:
            yield scrapy.Request(url=item['urls'], meta={'meta_1':item}, callback=self.second_parse)

    def second_parse(self, response):
        items = []
        meta_1 = response.meta['meta_1']
        son_urls = response.xpath("//ul//div[1]/div[1]/a/@href").extract()
        for i in range(0 ,len(son_urls)):
            son_url = 'https://www.shixiseng.com' + son_urls[i]
            item = ShixiItem()
            item['filename'] = meta_1['filename']
            item['son_urls'] = son_url
            items.append(item)
        for item in items:
            yield scrapy.Request(url=item['son_urls'], meta={'meta_2': item}, callback=self.third_parse)

    def third_parse(self, response):
        item = response.meta['meta_2']
        content = ''
        content_list = response.xpath("//div[1]/div[1]/div[2]/div/p//text() | // div[1]/div[2]/div[1]/div[3]/span/text()").extract()
        for content_one in content_list:
            content += content_one
        item['content'] = content
        yield item









