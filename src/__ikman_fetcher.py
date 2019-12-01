import sys
import logging
from Scrapper import Scrapper
from FileHandler import FileHandler
from customExceptions import ValueNotValidForFieldError

class Fetcher:
    def __init__(self,fileName):
        self.fileObject=FileHandler(fileName)
        self.langList=['en','si','ta']
        self.categories=['vehicles','property','vehicles']
        self.query=None
        self.language=None
        self.category=None

    # Get User inputs
    def getUserData(self):
        try:
            self.query= input("Enter query:")
            category= input("Enter category:")
            if category in self.categories:
                self.category=category
            else:
                raise ValueNotValidForFieldError
            lang=input("Enter language:")
            if lang in self.langList:
                self.language=lang
            else:
                raise ValueNotValidForFieldError
        except ValueNotValidForFieldError:
            print("Data entered is not valid")
            logging.error('Data entered is not valid') 
  
    # send data to file handler to write to json
    def fetchData(self,scObj):
        self.resulList=scObj.scrapeData(self.query,self.language, self.category)
        if len(self.resulList)>0:
            self.fileObject.writeToFile(self.resulList)
        else:
           logging.error('Not a valid querry String') 
           print("Not a valid querry String") 


def mainObjCreator():
    fetcherObj=Fetcher("output/output.json")
    fetcherObj.getUserData()
    scrObj=Scrapper()
    if fetcherObj.language is None or fetcherObj.category is None  or fetcherObj.query is None:
        print("Data provided is not enough to proceed") 
        logging.warning('Data provided is not enough to proceed')
    else:
        fetcherObj.fetchData(scrObj)

if __name__ == '__main__':
    mainObjCreator()
    
        
