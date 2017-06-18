# from scrapy.http import Request
import scrapy
from pstipspider.items import PstipspiderItem
from datetime import datetime

# from scrapy.selector import Selector


class PsTipSpider(scrapy.Spider):
    """
  Spider to scrape all the powershell postings from
  Hey!Scripting Guy
  """
    name = "pstip"
    start_urls = [
        "https://blogs.technet.microsoft.com/heyscriptingguy/page/%d/" % page
        for page in xrange(1, 10)
    ]

    def parse(self, response):
        query_article = "article.tag-powershell"
        for sel_article in response.css(query_article):
            title = sel_article.css("h2.entry-title a::text").extract_first()
            link = sel_article.css(
                "h2.entry-title a::attr(href)").extract_first()
            date = sel_article.css(
                "div.entry-content time.entry-date::text").extract_first()
            date_parsed = datetime.strptime(date, "%B %d, %Y")
            comments = sel_article.css(
                "div.entry-content span.comments-link a::text").extract_first()
            item = PstipspiderItem()
            item["Title"] = title
            item["Link"] = link
            item["Date"] = date_parsed
            item["Comments"] = int(comments)
            yield item