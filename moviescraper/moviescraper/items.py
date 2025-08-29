# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MoviescraperItem(scrapy.Item):
     
    title = scrapy.Field()
    director = scrapy.Field()
    cast = scrapy.Field()
    genre = scrapy.Field()
    notes = scrapy.Field()
   
    
    