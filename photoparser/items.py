import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader
from itemadapter import ItemAdapter

# def process_photo_url(value):
# Ссылки в лоадере 'photos' у меня не на те фото что нужно
# Была идея заменить значения w и h в ссылке на 1200, но я не знаю как это реализовать
# https://res.cloudinary.com/lmru/image/upload/f_auto,q_auto,w_1200,h_1200,c_pad,b_white,d_photoiscoming.png/LMCode/93871601_04.jpg

# def process_price(value):
#     value = int(item['price'])
#     return value
#  не получилось привести к числовому типу

class PhotoparserItem(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose())
    price = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field()
    _id = scrapy.Field()

