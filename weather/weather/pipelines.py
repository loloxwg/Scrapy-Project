# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import os,json

pathdir = os.getcwd()
class WeatherPipeline(object):
    def process_item(self, item, spider):
        # 文件存在data目录下的weather.txt文件内
        fiename = pathdir + '\\data\\weather.txt'
        # 从内存以追加的方式打开文件，并写入对应的数据
        with open(fiename, 'a', encoding='utf8') as f:
            # f.write('地区:' + item['location'] + '\n')
            for i in range(7):
                f.write('------------' + str(item['location']) + '-----------------' + '\n')
                f.write('日期:' + item['date'][i] + '\n')
                f.write('星期:' + item['week'][i] + '\n')
                f.write('最高温度:' + item['high_temperature'][i] + '\n')
                f.write('最低温度' + item['low_temperature'][i] + '\n')
                f.write('天气:' + item['weather'][i] + '\n')
                f.write('风况:' + item['wind'][i] + '\n')


        return item

class W2json(object):
    def process_item(self, item, spider):
        '''
        讲爬取的信息保存到json
        方便调用
        '''
        filename = pathdir + '\\data\\weather.json'

        # 打开json文件，向里面以dumps的方式吸入数据
        # 注意需要有一个参数ensure_ascii=False ，不然数据会直接为utf编码的方式存入比如:“/xe15”
        with open(filename, 'a', encoding='utf8') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)

        return item