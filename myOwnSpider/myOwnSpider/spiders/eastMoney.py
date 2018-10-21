# -*- coding: utf-8 -*-
import scrapy


class EastmoneySpider(scrapy.Spider):
    name = 'eastMoney'
    allowed_domains = ['finance.eastmoney.com']
    start_urls = ['http://finance.eastmoney.com/']

    def parse(self, response):
        pass
