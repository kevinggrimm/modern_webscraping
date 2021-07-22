import scrapy
import logging

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
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # Always return data as a dict
            # yield {
            #     'country_name': name,
            #     'country_link': link
            # }

            # absolute_url = f"https://www.worldometers.info{link}"
            # absolute_url = response.urljoin(link)
            # yield scrapy.Request(url=absolute_url)

            yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})

    def parse_country(self, response):
        # logging.info(response.url)
        name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")

        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            yield {
                'country_name': name,
                'year': year,
                'population': population
            }