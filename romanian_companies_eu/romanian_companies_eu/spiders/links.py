from scrapy.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

class MySpider(CrawlSpider):
    name = "links"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/npo"]

    rules = (
        # Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_items", follow= True),
        # Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//div[contains(@class, "pagination")]')), callback='parse_items', follow=True),
    )

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath('//span[@class="pl"]')
        items = []
        for titles in titles:
            print(titles.xpath("a/@href").extract())

