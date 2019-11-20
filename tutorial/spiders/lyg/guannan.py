# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import GovNewsItem

# scrapy crawl guannan
class GuannanSpider(scrapy.Spider):
    """灌南"""
    name = 'guannan'
    allowed_domains = ['guannan.gov.cn']
    map = {"公示公告":"http://www.guannan.gov.cn/gnzx/gsgg/gsgg.html",
           "灌南要闻":"http://www.guannan.gov.cn/gnzx/gnyw/gnyw.html",
           "部门信息":"http://www.guannan.gov.cn/gnzx/bmxx/bmxx.html"}
    start_urls = map.values()

    def parse(self, response):
        ul = response.css(".lb_con .right ul")
        # d1 = response.css('ul[id="tp"]')
        for li in ul:
            item = GovNewsItem()
            item["title"] = li.css('a::attr(title)').extract_first()
            url = li.css('a::attr(href)').extract_first()
            item["url"] = response.urljoin(url)
            item["time"] = li.css('span::text').extract_first()
            list = url.split("/")
            item["uuid"] = list[len(list)-1].split(".")[0]
            yield item

