

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
            next_page = response.css('li.next a::attr(href)').extract_first()
	        if next_page is not None:
	            next_page = response.urljoin(next_page)
	            yield scrapy.Request(next_page, callback=self.parse)


# class AuthorSpider(scrapy.Spider):
#     name = 'author'

#     start_urls = ['http://quotes.toscrape.com/']

#     def parse(self, response):
#         # follow links to author pages
#         for href in response.css('.author + a::attr(href)'):
#             yield response.follow(href, self.parse_author)

#         # follow pagination links
#         for href in response.css('li.next a::attr(href)'):
#             yield response.follow(href, self.parse)

#     def parse_author(self, response):
#         def extract_with_css(query):
#             return response.css(query).extract_first().strip()

#         yield {
#             'name': extract_with_css('h3.author-title::text'),
#             'birthdate': extract_with_css('.author-born-date::text'),
#             'bio': extract_with_css('.author-description::text'),
#         }
	            

