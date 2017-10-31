

import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = "aaa"
#     start_urls = [
#         'http://quotes.toscrape.com/page/1/',
#        # 'http://quotes.toscrape.com/page/2/',
#     ]

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = 'quotes-%s.html' % page
#         with open(filename, 'wb') as f:
#             f.write(response.body)

class QuotesSpider(scrapy.Spider):
    name = "aaa"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
       # 'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
    	page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            #f.write(response.body)
	        for quote in response.css('.text'):
	        	yield{

                	'text' : quote.css('::text').extract()
	        	}
             	#f.writelines(a)
	            

