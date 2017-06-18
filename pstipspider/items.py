# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from datetime import datetime


def to_isoformat(dt):
    assert isinstance(dt, datetime)
    return dt.date.isoformat()


class PstipspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = scrapy.Field()
    Link = scrapy.Field()
    Date = scrapy.Field(output_processor=to_isoformat)
    Comments = scrapy.Field()
