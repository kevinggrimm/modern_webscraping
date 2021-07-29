import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    
    ## This can be commented out when start_request is overwritten in the Spider 
    # start_urls = ['https://www.imdb.com/chart/top/']

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"

    # When you overwrite start_request, you dont have to specify a callback method inside the request class
    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/chart/top/', 
            # user-agent would only be changed for this first request
            headers={
                'User-Agent': self.user_agent
            }
        )

    
    rules = (
        # `allow` => follow and parse items if link contains 'Items'
        # `restrict_xpaths`=('//a[@class="active"]`) ==> follow 'a' elements that are active
        Rule(LinkExtractor(restrict_xpaths="//td[@class='titleColumn']/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
        
        # Next link URLs
        # - This is called 2nd because we want the URL for each movie to be scraped first
        # - No callback is required because, when the next page loads, the first Rule will be
        # executed, which is what we want - for each movie page to be targeted

        # NOTE - Commenting out bc IMBD changed their format (now all on one page)
        # Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"), process_request='set_user_agent')
    )

    # `spider` argument is required for Scrapy 2.0+
    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    """
    XPath functions:
    - `normalize_space()` ==> Trims space
    - ``
    """
    def parse_item(self, response):
        # print(response.url)
        yield {
            'title': response.xpath("//h1[contains(@class,'TitleHeader')]/text()").get(),
            'year': response.xpath("//span[starts-with(@class,'TitleBlockMetaData')]//text()").get(),
            'duration': response.xpath("//li[contains(text(),'min') and contains(@role, 'presentation')]/text()").get(),
            'genre': response.xpath("//a[starts-with(@class,'GenresAndPlot')]/span/text()").get(),
            'rating': response.xpath("//span[contains(@class,'RatingScore')]/text()").get(),
            'movie_url': response.url
            # 'user-agent': response.request.headers['User-Agent']
        }