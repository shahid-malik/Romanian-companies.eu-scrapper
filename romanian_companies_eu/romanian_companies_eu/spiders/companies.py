# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from romanian_companies_eu.items import CompanyItem
from scrapy.http import Request


class CompaniesSpider(CrawlSpider):
    """This spider parse the romanian-companies.eu website and get all the urls of
    indivdual companies which would be used later to scrape company urls"""
    name = 'companies'
    allowed_domains = ["www.romanian-companies.eu"]

    def start_requests(self):
        """Send request to all the pages from 1 to 15334"""
        done_list = []
        for x in xrange(1, 15334):
            if x not in done_list:
                done_list.append(x)
                yield Request('https://www.romanian-companies.eu/pagini/p'+str(x)+'.htm', dont_filter=True)
            else:
                pass

    def parse(self, response):
        """
        Parse every single company url and send to the database
        """
        item = CompanyItem()
        if response.status != 200:
            yield scrapy.Request(url=response.url, dont_filter=True)

        try:
            company_urls = response.css('tr.clickable-row a::attr(href)').extract()
            company_names = response.css('tr.clickable-row a::attr(title)').extract()
            for name, url in zip(company_names, company_urls):
                item['name'] = name
                item['website'] = str('https://www.romanian-companies.eu'+url).strip()
                yield item
        except Exception as e:
            print("Company url and Company name url get Exception: ", e)
