# -*- coding: utf-8 -*-
import scrapy
from ..items import FilmItem

class DianyingSpider(scrapy.Spider):
    name = 'dianying'
    allowed_domains = ['www.dy2018.com']
    #获取科幻电影下的信息
    start_urls = ['https://www.dy2018.com/4/']

    def parse(self, response):
        tables = response.xpath('//table[@class="tbspan"]')
        for table in tables:
            item = FilmItem()
            #在此不能使用tbody标签进行抓取，抓取结果为none
            href = table.xpath('.//a[@class="ulink"][2]/@href').extract_first()
            title = table.xpath('.//a[@class="ulink"][2]/@title').extract_first()

            item['title'] = title
            #https: // www.dy2018.com / i / 99821.html
            movie_detail = 'https://www.dy2018.com' + href
            yield scrapy.Request(url=movie_detail,callback=self.parse2,meta={'key':item})

    def parse2(self,response):
        item = response.meta['key']

        movie_download_url = response.xpath('//td[@bgcolor="#fdfddf"]//a/@href').extract()

        item['movie_download_url'] = movie_download_url[-1]

        yield item