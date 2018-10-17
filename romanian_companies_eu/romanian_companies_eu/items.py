# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RomanianCompaniesEuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


from scrapy.item import Item, Field

class CompanyItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    desc = scrapy.Field()
    category = scrapy.Field()