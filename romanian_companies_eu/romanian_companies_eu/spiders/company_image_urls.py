# -*- coding: utf-8 -*-
import scrapy
import MySQLdb
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from romanian_companies_eu.items import CompanyItem


class CompaniesURLSpider(CrawlSpider):
    """
    This company will scrape all those website links which have images as url of the company
    """
    name = 'companies_image_url'
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
        """
            Send requests to all those urls which have images as url of the company

        :return:
        """
        try:
            # query = "select website from company where status is null ORDER BY id asc limit 10000"
            query = "select website from company2 where web_addr = 'Web Address';"
            self.cursor.execute(query)
            numrows = self.cursor.rowcount
            for x in xrange(0, numrows):
                row = self.cursor.fetchone()
                detailed_pag_url = str(row[0])
                yield scrapy.Request(url=detailed_pag_url, callback=self.parse)
        except MySQLdb.Error, e:
            print("Database connection Error", e)

    def parse(self, response):
        """
        Parse company website address from the images
        :param response:
        :return:
        """
        item = CompanyItem()
        web_addr = ''
        try:
            web_addr = response.css('img.img-thumbnail::attr(src)').extract()[0].split('/')[-1][:-4]
            status = 'image done'
        except Exception as e:
            print("Image get Exception", e)
            status = ''
        item['website'] = str(response.url)
        item['web_addr'] = str(web_addr).strip()
        item['status'] = status
        yield item



