

import scrapy
#from tutorial.items import StockPriceItem
from ..items import StockPriceItem

class StockPriceSpider(scrapy.Spider):
    name = "StockPriceSpider"
    custom_settings = {
    'ITEM_PIPELINES':{'tutorial.pipeline.JsonWriterPipeline': 10,},
    }

    def __init__(self, *args, **kwargs):
        self.start_urls = [args[0][0],]
        self.code = args[0][1]

    # start_urls = [
    #     'https://gupiao.baidu.com/stock/sh600111.html',
    # ]

    def parse(self, response):
        #items = []
        for quote in response.css('strong'):
            item = StockPriceItem()
            item['price'] = quote.css('::text').extract()
            item['code'] = self.code
            return item
            #items.append(item)
        return items
