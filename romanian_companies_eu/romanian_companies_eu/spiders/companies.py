# -*- coding: utf-8 -*-
import os
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from romanian_companies_eu.items import CompanyItem
from scrapy.http import Request


class CompaniesSpider(CrawlSpider):
    name = 'companies'
    allowed_domains = ["www.romanian-companies.eu"]

    # start_urls = [
    #     "https://www.romanian-companies.eu/pagini/p2800.htm"
    # ]
    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths="(//div[@class='text-center']/ul/li)"), callback="parse_item"),
    # )
    def start_requests(self):
        done_list = []
        for x in xrange(11000, 15334):
            if x not in done_list:
                print(x)
                done_list.append(x)
                yield Request('https://www.romanian-companies.eu/pagini/p'+str(x)+'.htm', dont_filter=True)
            else:
                pass

    def parse(self, response):
        item = CompanyItem()
        if response.status !=200:
            yield scrapy.Request(url=response.url, dont_filter=True)

        try:
            company_urls = response.css('tr.clickable-row a::attr(href)').extract()
            company_names = response.css('tr.clickable-row a::attr(title)').extract()
            for name, url in zip(company_names, company_urls):
                item['name'] = name
                item['website'] = str('https://www.romanian-companies.eu'+url).strip()
                yield item
            # yield scrapy.Request(url=response.url, dont_filter=True)
        except Exception as e:
            print("Exception: ", e)