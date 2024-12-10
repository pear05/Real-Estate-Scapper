# beautifulsoup4: Used for parsing HTML and XML documents.
# requests: Used for making HTTP requests to websites.
# scrapy: A powerful framework for large-scale web scraping.

import scrapy

class RealEstateSpider(scrapy.Spider):
    name = 'real_estate'
    allowed_domains = ['example.com']  # Replace with your target domain
    start_urls = ['https://www.example.com/listings']

    def parse(self, response):
        property_links = response.css('a.property-link::attr(href)').extract()

        for link in property_links:
            yield response.follow(link, callback=self.parse_property)

    def parse_property(self, response):
        yield {
            'title': response.css('h1.property-title::text').get(),
            'price': response.css('span.price::text').get(),
            'address': response.css('p.address::text').get(),
            # ... other fields
        }