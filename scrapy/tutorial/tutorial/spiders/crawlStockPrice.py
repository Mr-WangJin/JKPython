

import scrapy
from tutorial.items import StockPriceItem

class StockPriceSpider(scrapy.Spider):
    name = "StockPriceSpider"

    def __init__(self, *args, **kwargs):
        self.start_urls = [args[0],]

    # start_urls = [
    #     'https://gupiao.baidu.com/stock/sh600111.html',
    # ]

    def parse(self, response):
        items = []
        for quote in response.css('strong'):
            item = StockPriceItem()
            item['price'] = quote.css('::text').extract()
            items.append(item)
        return items
