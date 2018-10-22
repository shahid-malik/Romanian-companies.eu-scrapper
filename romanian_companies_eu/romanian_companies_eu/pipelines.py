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
    """
    Method to process the item and put company urls into company table
    """
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', 'root', 'romanian_companies',
                                    charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        """
        Method to process the data
        :param item: Scrapy item
        :param spider:  Spider name
        :return:
        """
        try:
            query = "INSERT INTO company (name, website)  VALUES " \
                    "("'"%s"'", "'"%s"'")" % (str(item['name'].encode('utf-8')),
                                              str(item['website'].encode('utf-8'))
            )
            print(query)
            self.cursor.execute(query)
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item


class CompanyURLPipeline(object):
    """
    This pipeline process the items coming from individual company urls visited in company_url spider
    """
    def __init__(self):
            self.conn = MySQLdb.connect('localhost', 'root', 'root', 'romanian_companies',
                                        charset="utf8", use_unicode=True)
            self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        """
        Process method for individual method. It will process item
        and save the company url to web_addr column of company table
        :param item:
        :param spider:
        :return:
        """
        try:
            website = str(item['website'].encode('utf-8'))
            try:
                url2 = str(item['url2'].encode('utf-8'))
            except:
                url2 = str(item['url2'])
            web_addr = str(item['web_addr'].encode('utf-8'))
            status = str(item['status'].encode('utf-8'))
            query = "UPDATE company SET url2 = '%s', web_addr = '%s', status= '%s' where website= '%s' " \
                    % (url2, web_addr, status, website)
            self.cursor.execute(query)
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item


class CompanyImageURLPipeline(object):
    """
    This pipeline will process those urls where company image has the website url of company
    """
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', 'root', 'romanian_companies',
                                    charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        """
        Main process method
        :param item: company item
        :param spider: Image_url Spider
        :return:
        """
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