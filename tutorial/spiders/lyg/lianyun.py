# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import GovNewsItem

# scrapy crawl lianyun
class LianYunSpider(scrapy.Spider):
    """连云"""
    name = 'lianyun'
    allowed_domains = ['lianyun.gov.cn']
    map = {"通知公告":"http://www.lianyun.gov.cn/lyq/tzgg/tzgg.html",
           "全市要闻":"http://www.lianyun.gov.cn/lyq/qsyw/qsyw.html",
           "连云要闻":"http://www.lianyun.gov.cn/lyq/jrly/jrly.html",
           "头条新闻":"http://www.lianyun.gov.cn/lyq/ttxw/ttxw.html"}
    start_urls = map.values()

    def parse(self, response):
        ul = response.css('.list_main ul')
        for li in ul:
            item = GovNewsItem()
            item["title"] = li.css('a::attr(title)').extract_first()
            url = li.css('a::attr(href)').extract_first()
            item["url"] = response.urljoin(url)
            item["time"] = li.css('span::text').extract_first().replace("[","").replace("]","")
            list = url.split("/")
            item["uuid"] = list[len(list)-1].split(".")[0]
            yield item