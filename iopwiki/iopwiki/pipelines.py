# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline
from urllib.parse import unquote

class IopwikiPipeline(FilesPipeline):
    # def process_item(self, item, spider):
    #     return item

    def file_path(self, request, response=None, info=None, *, item=None):
        url = request.url.replace("costume", "skin")
        file_name = item["doll_id"].zfill(4) + "-" + unquote(url.split("/")[-1])
        # file_name = item["doll_id"] + "-" + item["doll_name"] + "-" + unquote(request.url.split("/")[-1])
        # file_name = item["file_name"]
        return file_name
