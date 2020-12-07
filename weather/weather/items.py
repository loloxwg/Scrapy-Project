# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    location=scrapy.Field()
    date = scrapy.Field()
    week = scrapy.Field()
    high_temperature = scrapy.Field()
    low_temperature = scrapy.Field()
    weather = scrapy.Field()
    wind = scrapy.Field()
