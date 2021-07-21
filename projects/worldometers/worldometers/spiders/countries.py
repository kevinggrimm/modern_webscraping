import scrapy

"""
Each spider has a unique name
Can have multiple spiders per project

`allowed_domains` => Limits scope of links to scrape
- NOTE: Never add 'http://' at the start

`start_urls` => Links that we want to scrape
- By default, Scrapy uses HTTP - overwrite for list items

`parse` => Pass response we get back from Spider
- Can catch the response in the parse method
"""
class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        title = response.xpath("//h1/text()").get()
        countries = response.xpath("//td/a/text()").getall()

        # Always return data as a dict
        yield {
            'title': title,
            'countries': countries
        }
