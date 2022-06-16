from abc import ABC, abstractmethod
import os
import string
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import firefox
from selenium import webdriver

from support.article.Article import Article
from model.Article import Article as ArticleModal



class NewsSite(ABC):
    def __init__(self,base_url:string,last_index_page_id:int,category:int):
        self.base_url = base_url
        self.last_index_page_id = last_index_page_id
        self.category = category
    
    @abstractmethod
    def getLink(self,webElement:WebElement):
        """
        This abstract method should return a string
        :rtype: string
        """
        pass

    @abstractmethod
    def getElements(self,webDriver):
        """
        This abstract method should return a string
        :rtype: string
        """
        pass

    def __getWebDriver(self,url:string):

        firefox_options = firefox.options.Options()
        firefox_options.set_preference('browser.download.folderList', 2)
        firefox_options.set_preference('browser.download.manager.showWhenStarting', False)
        firefox_options.set_preference('browser.download.dir', os.getcwd())
        firefox_options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
        firefox_options.binary_location = '/opt/firefox/firefox'

        browser = webdriver.Firefox(options=firefox_options)
        browser.get(url)
        time.sleep(3) #to fix Message: Failed to read marionette port issue
        return browser
    

    def getLinks(self,store_enabled:bool=False):


        linkList = []
        page_numbers = [*range(30, self.last_index_page_id*30, 30)]
        page_numbers.insert(0,0)

        for page_number in page_numbers:
            

            if page_number <= 80*30:# to not to create duplicate records
                continue    

            new_url = self.base_url+"/"+str(page_number)
            elements = self.getElements(self.__getWebDriver(new_url))

            if len(elements) == 0:
                break

            for element in elements:
                title = ""
                url = self.getLink(element)
                category = self.category
                article = Article(title,url,category)

                if store_enabled:
                    print(article.dic())
                    self.__store_article(article)
                    
                linkList.append(article)
            
        return linkList
    
    def store_articles(self):
        self.getLinks(True)


    def __store_article(self,article:Article):
        (ArticleModal()).insert(article)