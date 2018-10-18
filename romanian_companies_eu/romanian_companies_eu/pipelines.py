# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request


class RomanianCompaniesEuPipeline(object):
    def process_item(self, item, spider):
        return item


# class CompanyPipeline(object):
#
#     def process_item(self, item, spider):
#         print("From pipeline", item)


class CompanyPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', 'root', 'romanian_companies',
                                    charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            query = "INSERT INTO company (id, name, website, parent_company)  VALUES " \
                    "(%s, "'"%s"'", "'"%s"'", "'"%s"'")" % (
                item['id'].encode('utf-8'),
                str(item['name'].encode('utf-8')),
                str(item['url'].encode('utf-8')),
                str(item['category'].encode('utf-8'))
            )
            print(query)

            self.cursor.execute(query)
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item