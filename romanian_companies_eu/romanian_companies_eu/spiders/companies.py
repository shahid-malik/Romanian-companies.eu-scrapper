# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from romanian_companies_eu.romanian_companies_eu.items import CompanyItem


class CompaniesSpider(CrawlSpider):
    name = 'companies'
    # allowed_domains = ['www.romanian-companies.eu/firme-domenii.asp?url=/top-firme.asp']
    # start_urls = ['https://www.romanian-companies.eu/firme-domenii.asp?url=/top-firme.asp/']
    allowed_domains = ["www.romanian-companies.eu"]

    # get all the pages of a company
    # start_urls = ['https://www.romanian-companies.eu/01/d1.htm']
    start_urls = []
    for page in range (1,100):
        url = "https://www.romanian-companies.eu/%s/d1.htm" % str(page).zfill(2)
        start_urls.append(url)

    # start_urls = get_start_urls(10)
    rules = (
        Rule(LinkExtractor(restrict_xpaths = "(//div[@class='text-center']/ul/li)"), callback="parse_item"),
    )

    # def start_requests(self):
    #     for page in range (1,100):
    #         yield Request("https://www.romanian-companies.eu/%s/d1.htm" % str(page).zfill(2))

    def parse_item(self, response):
        try:
            page_num = int((str(response).split('/')[-1]).split('.')[0][1:])
            with open('test.csv', 'a') as f:
                f.write(str(page_num))
                f.write('\n')

            yield scrapy.Request(url=response.url, dont_filter=True)
        except Exception as e:
            print("Exceptions", e)

        #
        #

        # yield scrapy.Request(url=response.request.url, meta={'index': response.meta['index']}, dont_filter=True)
    # def parse(self, response):
    #     print(response)
        # company_category  = response.css('div.panel-body::text').extract()[3]
        # print(company_category)
        # dir_path = self.create_data_directory()
        # file_name = self.create_company_file(company_category, dir_path)


















    # def create_company_file(self, company_category, dir_path):
    #     file_name = dir_path + '/' + company_category + '.csv'
    #     with open(file_name, "w") as empty_file:
    #         pass
    #     return empty_file
    #
    # def create_data_directory(self):
    #     dir_path = 'data'
    #     dir_exists = os.path.isdir(dir_path)
    #     if not dir_exists:
    #         os.makedirs(dir_path)
    #     return dir_path
