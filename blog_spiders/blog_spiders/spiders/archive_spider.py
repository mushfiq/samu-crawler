import scrapy
from blog_spiders.items import ArchiveItem

class PostSpider(scrapy.Spider):
    name = 'smw_archive'
    
    allowed_domains = ["somewhereinblog.net"]
    
    #build this list from the postid dynamically
    start_urls = [
        "www.somewhereinblog.net/blog/"
    ]
    
    def parse(self, response):
        for sel in response.xpath('//div[@id="rightpanel"]'):
            item = ArchiveItem()
            #fix it
            item['post_id'] = sel.xpath('//h1')
            yield item