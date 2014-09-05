# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class BlogSpidersItem(Item):
    # define the fields for your item here like:
    title = Field()
    date = Field()
    link = Field()
    description = Field()
    image = Field()
