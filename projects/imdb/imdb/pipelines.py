# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import pymongo

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

"""
Every pipeline can have two other methods
- open_spider(self, spider)
"""

class MongodbPipeline(object):
    collection_name = "best_movies"
    # Class Method
    # @classmethod
    # def from_crawler(cls, crawler):
    #     logging.warning(crawler.settings.get("MONGO_URI"))
    #     return cls()

    # Connect to Mongo DB + Database
    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://<USERNAME>:<PASSWORD>@cluster0.osan1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client["IMDB"]

        # Called when the spider is opened, or starts the execution
        logging.warning('SPIDER OPENED FROM PIPELINE')

    def close_spider(self, spider):
        self.client.close()
        # Called when the spider finishes scraping items
        logging.warning('SPIDER CLOSED FROM PIPELINE')

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item

