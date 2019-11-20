# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import GovNewsItem

# scrapy crawl guanyun
class GuanyunSpider(scrapy.Spider):
    """灌云"""
    name = 'guanyun'
    allowed_domains = ['guanyun.gov.cn']
    map = {"公示公告":"http://www.guanyun.gov.cn/gyxzf/gsgg/gsgg.html",
           "灌云要闻":"http://www.guanyun.gov.cn/gyxzf/gyyw/gyyw.html",
           "部门动态":"http://www.guanyun.gov.cn/gyxzf/bmdt/bmdt.html"}
    start_urls = map.values()

    def parse(self, response):
        d1 = response.css('ul[id="tp"]')
        for dd in d1:
            item = GovNewsItem()
            temp = dd.css('li[id="rp"]')
            item["title"] = temp.css('a::attr(title)').extract_first()
            url = temp.css('a::attr(href)').extract_first()
            item["url"] = response.urljoin(url)
            item["time"] = temp.css('a[id="time"]::text').extract_first()
            list = url.split("/")
            item["uuid"] = list[len(list)-1].split(".")[0]
            yield item
