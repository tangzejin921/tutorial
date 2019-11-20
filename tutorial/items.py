# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 相当于一个容器，和字典较像
class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MaoyanreyingItem(scrapy.Item):
    index = scrapy.Field()
    title = scrapy.Field()
    star = scrapy.Field()
    releasetime = scrapy.Field()
    score = scrapy.Field()

class GovNewsItem(scrapy.Item):
    """政府网站要闻"""
    title = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()
    uuid = scrapy.Field()