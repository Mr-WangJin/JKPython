# -*- coding: UTF-8 -*-

import sys
import scrapy
from scrapy.crawler import CrawlerProcess
from tutorial.spiders.crawlStockPrice import StockPriceSpider
from scrapy.utils.project import get_project_settings

def main(domain):
		process = CrawlerProcess(get_project_settings())
		process.crawl(StockPriceSpider, domain)
		process.start() # the script will block here until the crawling is finished
	
if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(sys.argv[1])
		sys.exit('ok')
	else:
		pass
	sys.exit('error')
	

	