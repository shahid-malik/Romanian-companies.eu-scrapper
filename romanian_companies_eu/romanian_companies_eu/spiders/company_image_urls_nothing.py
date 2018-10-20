# -*- coding: utf-8 -*-
import scrapy
import MySQLdb
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from romanian_companies_eu.items import CompanyItem


class CompaniesURLSpider(CrawlSpider):
    name = 'companies_image_urls_nothing'
    allowed_domains = ["www.romanian-companies.eu"]
    custom_settings = {
        'ITEM_PIPELINES': {
            "romanian_companies_eu.pipelines.CompanyImageURLPipeline": 401
        }
    }

    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', 'root', 'romanian_companies',
                                    charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def start_requests(self):
        try:
            # query = "select website from company where status is null ORDER BY id asc limit 10000"
            query = "select website from company2 where web_addr = 'nothing';"
            self.cursor.execute(query)
            numrows = self.cursor.rowcount
            for x in xrange(0, numrows):
                row = self.cursor.fetchone()
                detailed_pag_url = str(row[0])+'web-site.htm'
                print(detailed_pag_url)
                yield scrapy.Request(url=detailed_pag_url, callback=self.parse)
                if x == 40000:
                    print("**** Counter is at **** ", x)
                    break
        except MySQLdb.Error, e:
            print (e)

    def parse(self, response):
        item = CompanyItem()
        web_addr = ''
        try:
            web_addr = str(response.css('.text-center font::text').extract()[0])
            status = 'done3'
        except Exception as e:
            print("Exception", e)
            status = 'hello1'
        item['website'] = str(response.url[:-12])
        item['web_addr'] = str(web_addr).strip()
        item['status'] = status
        print(item)
        yield item



