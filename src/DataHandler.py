import requests
from lxml import html
import logging

class DataHandler:
    # Get xpath data Handler 
    def getDataFields(self,field,pageItem):
        switcher={
            'title':self.getTitle,
            'date':self.getDate,
            'shortDescription':self.getShortDescription,
            'category':self.getCategory,
            'fullDescription':self.getFullDescription,
            'price':self.getPrice,
            'contact':self.getContact,
            'imageList':self.getImageList   
            }
        func=switcher.get(field,'Invalid')
        return func(pageItem)

    # Extract requested data
    def getTitle(self,pageItem):
        try:
            return pageItem.xpath("//title/text()")[0] 
        except:
            logging.error('Get Title Error.') 

    # Extract requested data
    def getDate(self,pageItem):
        try:
            return pageItem.xpath("//p[@class='item-intro']/span[@class='date']/text()")[0] 
        except:
            logging.error('Get date Error.') 

    # Extract requested data
    def getShortDescription(self,pageItem):
        try:
            return pageItem.xpath("//h1[@itemprop='name']/text()")[0] 
        except:
            logging.error(f'Get short Description Error.') 

    # Extract requested data
    def getCategory(self,pageItem):
        try:
            return pageItem.xpath("//ol/li[6]/a/span[@itemprop='name']/text()")[0]
        except:
            logging.error('Get category Error.') 

    # Extract requested data
    def getFullDescription(self,pageItem):
        try:
            paragraphs=pageItem.xpath("//div[@class='item-description']/p")
            textdata=''
            for para in paragraphs:
                textdata=textdata.join(map(str.strip,para.xpath(".//text()")))
            return textdata
        except:
            logging.error('Get full description Error.') 
    # Extract requested data
    def getPrice(self,pageItem):
        try:
            return pageItem.xpath("//div[@class='ui-price-tag']/span[@class='amount']/text()")[0]
        except:
            logging.error('Get price Error.') 
    # Extract requested data
    def getContact(self,pageItem):
        try:
            return pageItem.xpath("//div[@class='item-contact-more is-showable']/ul/li/span/text()")
        except:
            logging.error('Get contact Error.') 
    # Extract requested data
    def getImageList(self,pageItem):
        try:
            return  pageItem.xpath("//div[@class='gallery-nav center-thumbnails']//img/@src")
        except:
            logging.error('Get image list Error.') 
          