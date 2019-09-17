# -*- coding: utf-8 -*-
import scrapy


class Doubantop250Spider(scrapy.Spider):
    name = 'doubantop250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        titles = response.xpath("//span[@class='title'][1]/text()").extract()
        print(titles)