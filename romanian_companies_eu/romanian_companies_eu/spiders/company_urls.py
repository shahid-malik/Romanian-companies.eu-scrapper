# -*- coding: utf-8 -*-
import scrapy
import MySQLdb
from scrapy.spiders import Rule, CrawlSpider
from romanian_companies_eu.items import CompanyItem


class CompaniesURLSpider(CrawlSpider):
    name = 'companies_url'
    allowed_domains = ["www.romanian-companies.eu"]
    custom_settings = {
        'ITEM_PIPELINES': {
            "romanian_companies_eu.pipelines.CompanyURLPipeline": 400
        }
    }

    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', 'root', 'romanian_companies',
                                    charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def start_requests(self):
        try:
            query = "select website from company2 where status is null"
            self.cursor.execute(query)
            numrows = self.cursor.rowcount
            for x in xrange(0, numrows):
                row = self.cursor.fetchone()
                detailed_pag_url = str(row[0])
                yield scrapy.Request(url=detailed_pag_url, callback=self.parse)
        except MySQLdb.Error, e:
            print (e)

    def parse(self, response):
        item = CompanyItem()
        try:
            try:
                company_top = str(response.css('h1#top::text')[0].extract())
            except:
                company_top = str((response.css('h1#top::text')[0].extract()).encode('utf8'))
            try:
                company_web = str(response.css('table#contact tr td::text')[-1].extract())
            except:
                print('company Name web Address Exception')
                company_web = 'Restricted'
            item['website'] = str(response.url)
            item['url2'] = str(company_top).strip()
            item['web_addr'] = str(company_web).strip()
            if company_web:
                item['status'] = "done"
            else:
                item['status'] = ''
            yield item

        except Exception as e:
            print("Parsing Exception", e)


