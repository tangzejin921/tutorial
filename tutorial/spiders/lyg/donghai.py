# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import GovNewsItem

# scrapy crawl donghai
class DonghaiSpider(scrapy.Spider):
    """东海"""
    name = 'donghai'
    allowed_domains = ['jsdh.gov.cn']
    map = {"公示公告":"http://www.jsdh.gov.cn/dhxzf/gsgg/gsgg.html",
           "东海新闻":"http://www.jsdh.gov.cn/dhxzf/dhxw/dhxw.html",
           "部门动态":"http://www.jsdh.gov.cn/dhxzf/bmdt/bmdt.html"}
    start_urls = map.values()

    def parse(self, response):
        ul = response.css('ul[class="xxgk-list-con"]')
        for li in ul:
            item = GovNewsItem()
            temp = li.css('span[class="wzbt"]')
            item["title"] = temp.css('a::attr(title)').extract_first()
            url = temp.css('a::attr(href)').extract_first()
            item["url"] = response.urljoin(url)
            item["time"] = li.css('span[class="wzrq"]::text').extract_first()
            list = url.split("/")
            item["uuid"] = list[len(list)-1].split(".")[0]
            yield item
