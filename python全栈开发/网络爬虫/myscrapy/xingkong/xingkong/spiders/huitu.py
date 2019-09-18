# -*- coding: utf-8 -*-
import scrapy
from xingkong.items import XingkongItem


class HuituSpider(scrapy.Spider):
    name = 'huitu'
    allowed_domains = ['www.huitu.com/']
    start_urls = ['http://soso.huitu.com/search?kw=星空']

    def parse(self, response):
        imgurls = response.xpath("//div[@class='seozone']/a/img/@originalsrc").extract()
        for url in imgurls:
            item = XingkongItem()
            item['image_urls'] = [url]
            yield item
