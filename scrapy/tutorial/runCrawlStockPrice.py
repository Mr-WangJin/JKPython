# -*- coding: UTF-8 -*-

import sys
import thread
import time
import scrapy
from scrapy.crawler import CrawlerProcess
from tutorial.spiders.crawlStockPrice import StockPriceSpider
from scrapy.utils.project import get_project_settings

def main(tupleParam):
	try:
		setting = get_project_settings()

		print(setting.__class__)
		print(isinstance(setting, dict))
		print '--------------------'
		process = CrawlerProcess(get_project_settings())
		process.crawl(StockPriceSpider, tupleParam)
		process.start() # the script will block here until the crawling is finished
		return '1'
	except Exception as e:
		print e.message
		return '0'

def crawlPrice(*args, **kwargs):
	print '--------------------------'
	print args
	param = [args[0], args[1]]
	return main(param)

	
if __name__ == '__main__':
	if len(sys.argv)  > 0:
		crawlPrice('https://gupiao.baidu.com/stock/sh600100.html', '600100')
		sys.exit('ok')
	else:
		pass
	sys.exit('error')




	