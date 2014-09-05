import scrapy
from blog_spiders.items import BlogSpidersItem

class PostSpider(scrapy.Spider):
    name = 'smw_post'
    
    allowed_domains = ["somewhereinblog.net"]
    
    #build this list from the postid dynamically
    start_urls = [
        "www.somewhereinblog.net/blog/"
    ]
    
    def parse(self, response):
        for sel in response.xpath('//div[@id="rightpanel"]'):
            item = BlogSpidersItem()
            item['title'] = sel.xpath('//h1')
            #fix it
            item['description'] = sel.xpath('//desc')
            item['image'] = sel.xpath('image')
            
            yield item