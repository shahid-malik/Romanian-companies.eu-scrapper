# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field


class RomanianCompaniesEuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CompanyItem(scrapy.Item):
    id = scrapy.Field()
    category = Field()
    name = scrapy.Field()
    url = scrapy.Field()
    pass