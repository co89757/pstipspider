# -*- coding: utf-8 -*-
import pstipspider.settings as proj_settings
from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PstipspiderPipeline(object):
    def process_item(self, item, spider):
        cutoff_yr = proj_settings.CUTOFF_YEAR
        if item.get("Date").year < cutoff_yr:
            raise DropItem(
                "Dropping item ({0}...) whose publish year is too old: {1}",
                item["Title"][:15], item["Date"].year)
        title_low = item["Title"].lower()
        if not ('power' in title_low):
            raise DropItem(
                "Dropping item that has no powershell keyword in it")
        return item