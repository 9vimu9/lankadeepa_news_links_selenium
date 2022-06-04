import string
from sites.NewsSite import NewsSite
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By



class Saravita(NewsSite):

    def __init__(self,base_url:string,last_index_page_id:int):
        super().__init__(base_url,last_index_page_id)

    def getLink(self,webElement:WebElement):
        return webElement.find_element_by_tag_name('a').get_attribute("href")
       
    def getElements(self,webDriver):
       return webDriver.find_elements(By.CLASS_NAME,'hero-feature')