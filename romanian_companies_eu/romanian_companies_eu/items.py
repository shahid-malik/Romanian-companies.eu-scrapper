# -*- coding: utf-8 -*-
import scrapy
from scrapy.item import Field


class CompanyItem(scrapy.Item):
    """
    Company Item with all the neccassary fields to be scrapped and store in the database
    """
    id = scrapy.Field()
    category = Field()
    name = scrapy.Field()
    website = scrapy.Field()
    url = scrapy.Field()
    status = scrapy.Field()
    url2 = scrapy.Field()
    web_addr =scrapy.Field()
    pass