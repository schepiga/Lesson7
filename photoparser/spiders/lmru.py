import scrapy
from scrapy.http import HtmlResponse
from photoparser.items import PhotoparserItem
from scrapy.loader import ItemLoader


class LmruSpider(scrapy.Spider):
    name = 'lmru'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, search_item):
        super(LmruSpider, self).__init__()
        self.start_urls = [f'https://leroymerlin.ru/search/?q={search_item}']

    def parse(self, response: HtmlResponse):
    # Не получилось перейти на другую сраницу
    #     next_page = response.xpath('//a[@data-qa-pagination-item="right"]/@href')
    #     if next_page:
    #         yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//a[@data-qa='product-name']")
        for link in links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=PhotoparserItem(), response=response)
        loader.add_xpath('name', '//h1/text()')
        loader.add_xpath('photos', "//picture/source[@media=' only screen and (min-width: 1024px)']/@data-origin")
        loader.add_xpath('price', '//span[@slot="price"]/text()')
        loader.add_value('url', response.url)

        yield loader.load_item()

