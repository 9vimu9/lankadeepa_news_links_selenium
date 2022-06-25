from abc import ABC, abstractmethod
import os
import string
import sys
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import firefox
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from model.Paragraph import Paragraph
from support.Constant import Constant
from support.Slack.ParagraphSaveFailed import ParagraphSaveFailed
from support.Slack.ParagraphSaved import ParagraphSaved
from support.article.Article import Article
from model.Article import Article as ArticleModal
from support.paragraph.ParagraphDTO import ParagraphDTO
from support.paragraph.ParagraphsDTO import ParagraphsDTO
import re



class NewsSite(ABC):
    def __init__(self,base_url:string,last_index_page_id:int,category:int):
        self.base_url = base_url
        self.last_index_page_id = last_index_page_id
        self.category = category
        self.driver = self.__initiate_web_driver()
    
    @abstractmethod
    def getLink(self,webElement:WebElement):
        pass

    @abstractmethod
    def extract_paragraphs(self,webDriver:WebDriver,article_id:int)-> ParagraphsDTO:
        pass

    @abstractmethod
    def validate_paragraph(self,paragraph:ParagraphDTO) -> bool:
        pass

    @abstractmethod
    def getElements(self,webDriver:WebDriver):
        pass

    def __getWebDriver(self,url:string):
        self.driver.get(url)
        time.sleep(10) #to fix Message: Failed to read marionette port issue
        return self.driver

    def __initiate_web_driver(self)->WebDriver:

        firefox_options = firefox.options.Options()
        firefox_options.add_argument('--headless')
        firefox_options.set_preference('browser.download.folderList', 2)
        firefox_options.set_preference('browser.download.manager.showWhenStarting', False)
        firefox_options.set_preference('browser.download.dir', os.getcwd())
        firefox_options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
        firefox_options.binary_location = '/opt/firefox/firefox'

        return webdriver.Firefox(options=firefox_options)

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
                    self.__store_article(article)
                    
                linkList.append(article)
            
        return linkList
    
    def store_articles(self):
        self.getLinks(True)


    def __store_article(self,article:Article):
        (ArticleModal()).insert(article)

    def store_paragraphs(self,article_count:int=sys.maxsize):
        for i in range(article_count):
            article = (ArticleModal()).get_fresh_article(self.category)

            if not article:
                break
            print(article.dic())
            self.__store_paragraph(article)
            print(i)


        

    def __store_paragraph(self,article:Article):
        try:
        
            paragraphsDTO = self.extract_paragraphs(self.__getWebDriver(article.url),article.id)
            paragraphsDTO = self.__merge_paragraphs(paragraphsDTO)
            paragraph_model = Paragraph()
            for paragraphDTO in paragraphsDTO.paragraphs:
                paragraphDTO.paragraph = self.__sanitize_paragraph(paragraphDTO.paragraph)

                if not self.validate_paragraph(paragraphDTO):
                    raise Exception("valiadtion error")
                
                paragraph_model.insert(paragraphsDTO.article_id,paragraphDTO.paragraph,paragraphDTO.order)
        except Exception as exception : 
            ArticleModal().update_paragraphs_added_status(article.id,Constant.ERROR_DURING_PARAGRAPH_PROCESS)
            ParagraphSaveFailed(exception).send()
            pass 
        
    def __sanitize_paragraph(self,paragraph:string)->str:
        paragraph = re.sub(r'^https?:\/\/.*[\r\n]*', '', paragraph, flags=re.MULTILINE)
        paragraph.strip()
        return paragraph

    def __merge_paragraphs(self,paragraphsDTO:ParagraphsDTO)->ParagraphsDTO:

        paragraph_max_character_threshold = 500
        
        paragraph_texts = []
        paragraphs_list = []

        for paragraphDTO in paragraphsDTO.paragraphs:
             if not self.validate_paragraph(paragraphDTO):
                 continue
             paragraph_texts.append(self.__sanitize_paragraph(paragraphDTO.paragraph))

        charater_count = [len(sentence) for sentence in paragraph_texts]
        total_character_count = sum(charater_count)

        if total_character_count < paragraph_max_character_threshold and total_character_count > 100  :
            paragraph = ' '.join(paragraph_texts)
            paragraphsDTO.paragraphs = [ParagraphDTO(paragraph,0)]
            return paragraphsDTO

        current_character_count = 0
        current_character_order = 0
        current_paragraph = ''
        # print(paragraph_texts)
        # raise SystemExit

        for index,text in enumerate(paragraph_texts):
            current_character_count += charater_count[index]
            current_paragraph += text

            if current_character_count > paragraph_max_character_threshold:
                paragraphs_list.append(ParagraphDTO(current_paragraph,current_character_order))
                current_character_order += 1
                current_character_count = 0
                current_paragraph = ''


        paragraphsDTO.paragraphs = paragraphs_list

        return paragraphsDTO
