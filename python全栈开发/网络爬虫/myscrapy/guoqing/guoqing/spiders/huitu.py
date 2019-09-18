# -*- coding: utf-8 -*-
import scrapy
from guoqing.items import GuoqingItem


class HuituSpider(scrapy.Spider):
    name = 'huitu'
    allowed_domains = ['soso.huitu.com']
    start_urls = ['http://soso.huitu.com/search?kw=国庆节']

    def parse(self, response):
        imgurls = response.xpath("//div[@class='seozone']/a/img/@originalsrc").extract()
        for url in imgurls:
            item = GuoqingItem()
            item["image_urls"] = [url]
            yield item