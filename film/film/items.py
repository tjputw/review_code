# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FilmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #首页获取
    title = scrapy.Field()
    #详情页面获取
    movie_download_url = scrapy.Field()

