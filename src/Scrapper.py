import requests
from lxml import html
from DataHandler import DataHandler
import logging

class Scrapper:
    
    def __init__(self):
        logging.basicConfig(level=logging.INFO,filename='logs/fetcher.log', format='%(name)s - %(levelname)s - %(message)s')
        self.baseUrl="https://ikman.lk"
        self.datahandler=DataHandler()
        
    # send request to fetch response data and create item list
    def scrapeData(self,query,language,category):
        self.query = query
        self.language = language
        self.category = category
        self.pageNumber=1
        self.url = self.baseUrl+"/"+self.language+"/ads/sri-lanka/"+self.category+"?by_paying_member=0&sort=relevance&buy_now=0&query="+self.query+"&page="+str(self.pageNumber)
        print(self.url)
        logging.info(f'scrapping data from URL: {self.url}')
        resp =self.sendRequest(self.url)
        tree=html.fromstring(html=resp.text)
        listdata=tree.xpath("//ul[@class='list--3NxGO']/li/a/@href|//ul[@class='list--3NxGO']/div/li/a[1]/@href")
        self.datalist=[]
        for item in listdata:
            respItem =self.sendRequest(self.baseUrl+item)
            pageItem=html.fromstring(html=respItem.text)
            self.datalist.append(self.addDataToJason(pageItem,self.baseUrl+item))
        return self.datalist

    # Get xpath data and pass to json       
    def addDataToJason(self,pageItem,url):
            title=self.datahandler.getDataFields('title',pageItem)
            date=self.datahandler.getDataFields('date',pageItem)
            shortDescription=self.datahandler.getDataFields('shortDescription',pageItem)
            category=self.datahandler.getDataFields('category',pageItem)
            fullDescription=self.datahandler.getDataFields('fullDescription',pageItem)
            price=self.datahandler.getDataFields('price',pageItem)
            contact=self.datahandler.getDataFields('contact',pageItem)
            imageList=self.datahandler.getDataFields('imageList',pageItem)

            itemjson={
                'title':title,
                'date':date,
                'shortDescription':shortDescription,
                'url':url,
                'category':category,
                'details':{
                    'fullDescription':fullDescription,
                    'image_urls':imageList,
                    'prince':price,
                    'contact':contact
                }
            }
            return itemjson

   

    
        
    # send request to fetch response data
    def sendRequest(self,url):
        try:
            res = requests.get(url)
            return res
        except requests.ConnectionError as e:
            print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
            print(str(e)) 
            logging.error(f'Connection Error.: {str(e)}')     
        except requests.Timeout as e:
            print("OOPS!! Timeout Error")
            logging.error(f'Timeout Error.: {str(e)}') 
        except requests.RequestException as e:
            print("OOPS!! General Error")
            print(str(e))
            logging.error(f'TGeneral Error.: {str(e)}') 
        except KeyboardInterrupt:
            print("execution interupted")
            logging.error(f'execution interupted.: {str(e)}') 
        