# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockPriceItem(scrapy.Item):
    # define the fields for your item here like:
    price = scrapy.Field()
    code = scrapy.Field()

    def printName(self):
        print(__name__)


    
