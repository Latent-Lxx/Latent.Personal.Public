# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class Yilongwang_List_Item(scrapy.Item):
    # define the fields for your item here like:
    projectId = scrapy.Field();



class Yilongwang_Comment_Item(scrapy.Item):
    # define the fields for your item here like:
    comment = scrapy.Field();
    name = scrapy.Field()

