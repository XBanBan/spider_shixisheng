# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShixiItem(scrapy.Item):
    filename = scrapy.Field()
    post = scrapy.Field()
    urls = scrapy.Field()
    son_urls = scrapy.Field()
    content = scrapy.Field()

