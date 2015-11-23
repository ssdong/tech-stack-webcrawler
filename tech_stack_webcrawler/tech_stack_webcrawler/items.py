# -*- coding: utf-8 -*-

# Define the models for scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TechStackWebcrawlerItem(scrapy.Item):
    tech = scrapy.Field()
    frequency = scrapy.Field() 
