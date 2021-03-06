# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Elo7Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    details = scrapy.Field()
    category = scrapy.Field()
    subcategory = scrapy.Field()
    url = scrapy.Field()
