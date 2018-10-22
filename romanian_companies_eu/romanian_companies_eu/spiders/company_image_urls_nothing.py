# -*- coding: utf-8 -*-
import scrapy
import MySQLdb
from scrapy.spiders import Rule, CrawlSpider
from romanian_companies_eu.items import CompanyItem


class CompaniesURLSpider(CrawlSpider):
    """
    This spider crawl all those company urls which have images
    and written nothing instead of url with image
    """
    name = 'companies_image_urls_nothing'
    allowed_domains = ["www.romanian-companies.eu"]
    custom_settings = {
        'ITEM_PIPELINES': {
            "romanian_companies_eu.pipelines.CompanyImageURLPipeline": 401
        }
    }

    def __init__(self):
        """
        Mysql connection in constructor to save the data
        """
        self.conn = MySQLdb.connect('localhost', 'root', 'root', 'romanian_companies',
                                    charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def start_requests(self):
        """
        Send individual request, data collected from mysql company table for those urls
        which has written nothing in place of url
        :return:
        """
        try:
            query = "select website from company2 where web_addr = 'nothing';"
            self.cursor.execute(query)
            numrows = self.cursor.rowcount
            for x in xrange(0, numrows):
                row = self.cursor.fetchone()
                detailed_pag_url = str(row[0])+'web-site.htm'
                yield scrapy.Request(url=detailed_pag_url, callback=self.parse)
        except MySQLdb.Error, e:
            print ("Mysql Connection Error", e)

    def parse(self, response):
        """
        Main parsing method
        :param response:
        :return:
        """
        item = CompanyItem()
        web_addr = ''
        try:
            web_addr = str(response.css('.text-center font::text').extract()[0])
            status = 'image done'
        except Exception as e:
            status = ''
        item['website'] = str(response.url[:-12])
        item['web_addr'] = str(web_addr).strip()
        item['status'] = status
        yield item



