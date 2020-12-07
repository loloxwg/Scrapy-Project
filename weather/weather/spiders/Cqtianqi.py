# -*- coding: utf-8 -*-
import scrapy

from weather.items import WeatherItem


class CqtianqiSpider(scrapy.Spider):
    name = 'CQtianqi'
    allowed_domains = ['tianqi.com']
    start_urls = []
    citys = ['chongqing', 'nananqu']
    for city in citys:
        start_urls.append('http://' + 'www.tianqi.com/' + city + '/')

    def parse(self, response):
        '''
        location=地区
        date = 当日日期
        week = 星期几
        wind = 当日风况
        weather = 当日天气
        high_temperature = 当日最高温度
        low_temperature = 当日最低温度
        :param response:
        :return:
        '''
        # oneweek = response.xpath('//div[@class="day7"]')
        #地区，日期，星期
        item = WeatherItem()
        location = response.xpath('//div[@class="top"]//h1/text()').extract()
        date = response.xpath('//div[@class="day7"]//ul[@class="week"]//li//b/text()').extract()
        week = response.xpath('//div[@class="day7"]//ul[@class="week"]//li//span/text()').extract()
        print(location)
        print(date)
        print(week)
        # 天气
        weather = response.xpath('//div[@class="day7"]//ul[@class="txt txt2"]//li/text()').extract()
        print(weather)
        # 最高气温，最低气温
        high_temperature = response.xpath('//div[@class="day7"]//div[@class="zxt_shuju"]/ul//li/span/text()').extract()
        low_temperature = response.xpath('//div[@class="day7"]//div[@class="zxt_shuju"]/ul//li/b/text()').extract()
        print(high_temperature)
        print(low_temperature)
        # 风向
        wind = response.xpath('//div[@class="day7"]//ul[@class="txt"][1]//li/text()').extract()
        print(wind)

        item['location'] = location
        item['date'] = date
        item['week'] = week
        item['weather'] = weather
        item['wind'] = wind
        item['high_temperature'] = high_temperature
        item['low_temperature'] = low_temperature
        yield item