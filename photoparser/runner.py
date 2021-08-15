from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from photoparser.spiders.lmru import LmruSpider
from photoparser import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    # input('Введите наименование')

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LmruSpider, search_item='матрас')

    process.start()