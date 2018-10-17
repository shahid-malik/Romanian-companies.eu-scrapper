# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractor import LinkExtractor

class CompaniesSpider(CrawlSpider):
    name = 'companies'
    allowed_domains = ['www.romanian-companies.eu']
    start_urls = ['https://www.romanian-companies.eu/firme-domenii.asp?url=/top-firme.asp']

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        pass
