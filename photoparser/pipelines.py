import scrapy
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient
from itemadapter import ItemAdapter


class PhotoparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client['leruaphotos15082021']

    def process_item(self, item, spider):
        print()
        collection_lerua = self.mongo_base[spider.name]
        collection_lerua.insert_one(item)
        return item

class LeruaPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item













