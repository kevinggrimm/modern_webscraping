import scrapy
from scrapy.exceptions import CloseSpider
import json

class EbooksSpider(scrapy.Spider):
    name = 'ebooks'

    INCREMENTED_BY = 12
    offset = 0

    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/subjects/picture_books.json?limit=12']

    def parse(self, response):

        if response.status == 500:
            raise CloseSpider('Reached last page of API')

        resp = json.loads(response.body)
        ebooks = resp.get('works')
        for ebook in ebooks:
            yield {
                'title': ebook.get('title'),
                'subject': ebook.get('subject'),
                'authors': [author.get('name') for author in ebook.get('authors')]
            }
        
        self.offset += self.INCREMENTED_BY
        # Need to set a condition for Spider to check before incrementing the offset
        # Check for status code = 500
        yield scrapy.Request(
            url=f"https://openlibrary.org/subjects/picture_books.json?limit=12&offset={self.offset}",
            callback=self.parse
        )