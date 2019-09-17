# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class Doubantop250Spider(scrapy.Spider):
    name = 'doubantop250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        for sel in response.xpath("//div[@class='info']"):
            item = DoubanItem()
            item['title'] = sel.xpath("div[@class='hd']/a/span[1]/text()")[0].extract()
            item['direct'] = sel.xpath("div[@class='bd']/p[1]/text()")[0].extract().strip()
            item['score'] = sel.xpath("div[@class='bd']/div/span[2]/text()")[0].extract()
            item['info'] = sel.xpath("div[@class='bd']/p[2]/span/text()")[0].extract()
            yield item
