# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import MaoyanreyingItem

# scrapy crawl maoyan
class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/board/7/']

    def parse(self, response):
        d1 = response.css(".board-wrapper dd")
        for dd in d1:
            item = MaoyanreyingItem()
            item["index"] = dd.css(".board-index::text").extract_first()
            item["title"] = dd.css(".name a::text").extract_first()
            item["star"] = dd.css(".star::text").extract_first()
            item["releasetime"] = dd.css(".releasetime::text").extract_first()
            item["score"] = dd.css(".integer::text").extract_first()+dd.css(".fraction::text").extract_first()
            yield item