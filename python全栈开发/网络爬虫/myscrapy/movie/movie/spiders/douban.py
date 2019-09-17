# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    index = 0
    url = 'https://movie.douban.com/top250?start='
    start_urls = ['https://movie.douban.com/top250?start=0']

    def parse(self, response):
        for sel in response.xpath("//div[@class='hd']"):
            url = sel.xpath("a/@href").extract()[0]
            yield scrapy.Request(url,callback=self.parseCon)

        self.index+=25
        if self.index<226:
            yield scrapy.Request(self.url+str(self.index),callback=self.parse)   

    def parseCon(self,response):
        # 详情
        title = response.xpath("//h1/span[1]/text()").extract()[0]
        print(title)
