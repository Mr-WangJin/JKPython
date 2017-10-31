

import json

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.json', 'w')

    def open_spider(self, spider):
        pass
        #self.file = open('items.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
