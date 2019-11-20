# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import GovNewsItem

# scrapy crawl lianyungang
class LianYunGangSpider(scrapy.Spider):
    """连云港"""
    name = 'lianyungang'
    allowed_domains = ['lyg.gov.cn']
    map = {"公示通告":"http://www.lyg.gov.cn/zglygzfmhwz/gsgg/gsgg.html",
           "政务要闻":"http://www.lyg.gov.cn/zglygzfmhwz/gcyw/gcyw.html",
           "部门信息":"http://www.lyg.gov.cn/zglygzfmhwz/bmdt/bmdt.html"}
    start_urls = map.values()

    def parse(self, response):
        ul = response.css('ul[class="xxgk-list-con"]')
        for li in ul:
            item = GovNewsItem()
            item["title"] = li.css('a::attr(title)').extract_first()
            url = li.css('a::attr(href)').extract_first()
            item["url"] = response.urljoin(url)
            item["time"] = li.css('span::text').extract_first()
            list = url.split("/")
            item["uuid"] = list[len(list)-1].split(".")[0]
            yield item