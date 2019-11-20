# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 定义Item Pipeline的实现，实现数据的清洗，储存，验证。
class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item
