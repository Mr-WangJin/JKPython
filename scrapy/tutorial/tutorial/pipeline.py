

import json
from tutorial.items import StockPriceItem

class JsonWriterPipeline(object):

    def __init__(self):
        pass
        #self.file = open('items.json', 'w')

    def open_spider(self, spider):
        pass
        #self.file = open('items.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        #self.file.close()
        pass

    def process_item(self, item, spider):
        print('------------open code file '+ item["code"])
        self.file = open(item["code"], 'w')
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        self.file.close()

        return item
