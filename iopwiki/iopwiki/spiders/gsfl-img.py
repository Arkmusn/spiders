from pathlib import Path

import scrapy
import re
from ..items import IopwikiItem as Item

root_path = "https://iopwiki.com"


class ImageSpider(scrapy.Spider):
    name = "image"

    def start_requests(self):
        # urls = ["https://iopwiki.com/wiki/9A-91"]
        urls = ["https://iopwiki.com/wiki/T-Doll_Index"]
        for url in urls:
            # yield scrapy.Request(url=url, callback=self.parse_doll)
            yield scrapy.Request(url=url, callback=self.parse_doll_index)

    def parse_doll_index(self, response):
        dolls = response.xpath("//span[@class=\"card-bg-small\"]/span/a/@href").getall()
        yield from response.follow_all(dolls, callback=self.parse_doll)

    def parse_doll(self, response):
        doll_id = response.xpath("//span[@class=\"indexnumber\"]/text()").get()
        doll_name = response.xpath("//h1[@id=\"firstHeading\"]/text()").get()
        image_file_paths = response.xpath("//li[@class=\"gallerybox\"]//a/@href").getall()
        pattern = re.compile("CHARACTER_SETTINGS|Wallpaper|_S\.png|Background")
        image_file_paths = list(filter(lambda path: pattern.search(path) is None, image_file_paths))
        yield from response.follow_all(image_file_paths, callback=self.parse_image_url,
                                       cb_kwargs=dict(doll_id=doll_id, doll_name=doll_name))

    def parse_image_url(self, response, doll_id, doll_name):
        node = response.xpath("//div[@class=\"fullMedia\"]/a/@href")

        image_path = node.get()
        item = Item()
        item["file_urls"] = [root_path + image_path]
        item["doll_id"] = doll_id
        item["doll_name"] = doll_name
        yield item
