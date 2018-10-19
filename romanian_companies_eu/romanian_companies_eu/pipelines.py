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


class CompanyURLPipeline(object):
    def __init__(self):
            self.conn = MySQLdb.connect('localhost', 'root', 'root', 'romanian_companies',
                                        charset="utf8", use_unicode=True)
            self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            website = str(item['website'].encode('utf-8'))
            url2 = str(item['url2'].encode('utf-8'))
            web_addr = str(item['web_addr'].encode('utf-8'))
            status = str(item['status'].encode('utf-8'))

            query = "UPDATE company SET url2 = '%s', web_addr = '%s', status= '%s' where website= '%s' " \
                    % (url2, web_addr, status, website)
            print(query)

            self.cursor.execute(query)
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item


class CompanyImageURLPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', 'root', 'romanian_companies',
                                    charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            website = str(item['website'].encode('utf-8'))
            web_addr = str(item['web_addr'].encode('utf-8'))
            status = str(item['status'].encode('utf-8'))

            query = "UPDATE company SET web_addr = '%s', status= '%s' where website= '%s' " \
                    % (web_addr, status, website)
            print(query)

            self.cursor.execute(query)
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item