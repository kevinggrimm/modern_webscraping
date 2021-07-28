import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    # start_urls = ['http://web.archive.org/web/20200715000935if_/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']
    start_urls = ['https://www.imdb.com/chart/top/']

    rules = (
        # `allow` => follow and parse items if link contains 'Items'
        # `restrict_xpaths`=('//a[@class="active"]`) ==> follow 'a' elements that are active
        Rule(LinkExtractor(restrict_xpaths="//td[@class='titleColumn']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print(response.url)
        yield {
            'title': response.xpath("//h1[contains(@class,'TitleHeader')]/text()").get(),
            'year': response.xpath("//span[starts-with(@class,'TitleBlockMetaData')]//text()").get(),
            'duration': response.xpath("//li[contains(text(),'min') and contains(@role, 'presentation')]/text()").get(),
            'genre': response.xpath("//a[starts-with(@class,'GenresAndPlot')]/span/text()").get(),
            'rating': response.xpath("//span[contains(@class,'RatingScore')]/text()").get(),
            'movie_url': response.url
        }