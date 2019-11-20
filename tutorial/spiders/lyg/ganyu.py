# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import GovNewsItem

# scrapy crawl ganyu
class GanYuSpider(scrapy.Spider):
    """赣榆"""
    name = 'ganyu'
    allowed_domains = ['guanyun.gov.cn']
    map = {"公示公告":"http://www.ganyu.gov.cn/gyqzf/gsgg/gsgg.html",
           "赣榆要闻":"http://www.ganyu.gov.cn/gyqzf/gyyw/gyyw.html",
           "工作动态":"http://www.ganyu.gov.cn/gyqzf/gzdt/gzdt.html"}
    start_urls = map.values()

    def parse(self, response):
        ul = response.css('ul[class="msg"]')
        for li in ul:
            item = GovNewsItem()
            item["title"] = li.css('a::attr(title)').extract_first()
            url = li.css('a::attr(href)').extract_first()
            item["url"] = response.urljoin(url)
            item["time"] = li.css('label::text').extract_first()
            list = url.split("/")
            item["uuid"] = list[len(list)-1].split(".")[0]
            yield item
