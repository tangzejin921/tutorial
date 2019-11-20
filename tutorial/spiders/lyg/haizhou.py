# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import GovNewsItem

# scrapy crawl haizhou
class HaiZhouSpider(scrapy.Spider):
    """海州"""
    name = 'haizhou'
    allowed_domains = ['lyghz.gov.cn']
    map = {"通知公告":"http://www.lyghz.gov.cn/lyghzqrmzf/tzggg/tzggg.html",
           "头条新闻":"http://www.lyghz.gov.cn/lyghzqrmzf/ttxw/ttxw.html",
           "海州要闻":"http://www.lyghz.gov.cn/lyghzqrmzf/hzyw/hzyw.html"}
    start_urls = map.values()

    def parse(self, response):
        ul = response.css('ul[class="listing"]')
        for li in ul:
            item = GovNewsItem()
            item["title"] = li.css('a::attr(title)').extract_first()
            url = li.css('a::attr(href)').extract_first()
            item["url"] = response.urljoin(url)
            item["time"] = li.css('span[class="date"]::text').extract_first()
            list = url.split("/")
            item["uuid"] = list[len(list)-1].split(".")[0]
            yield item