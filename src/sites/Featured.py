import string
from sites.NewsSite import NewsSite
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from support.Constant import Constant



class Featured(NewsSite):

    def __init__(self):
        super().__init__("https://www.lankadeepa.lk/sunday/rasawitha/57",Constant.MAX_PAGES_FOR_ARTICLE,Constant.ARTICLE_CATEGORY_FEATURED)

    def getLink(self,webElement:WebElement):
        return webElement.find_element_by_tag_name('a').get_attribute("href")

       
    def getElements(self,webDriver):
       return webDriver.find_elements(By.CLASS_NAME,'entry-title')
       