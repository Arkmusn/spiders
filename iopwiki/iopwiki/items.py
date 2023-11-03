# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IopwikiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    file_name = scrapy.Field()
    doll_id = scrapy.Field()
    doll_name = scrapy.Field()
