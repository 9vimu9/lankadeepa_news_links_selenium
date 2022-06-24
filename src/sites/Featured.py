from sites.NewsSite import NewsSite
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from support.Constant import Constant

from selenium.webdriver.firefox.webdriver import WebDriver

from support.paragraph.ParagraphDTO import ParagraphDTO
from support.paragraph.ParagraphsDTO import ParagraphsDTO



class Featured(NewsSite):

    def __init__(self):
        super().__init__("https://www.lankadeepa.lk/sunday/rasawitha/57",Constant.MAX_PAGES_FOR_ARTICLE,Constant.ARTICLE_CATEGORY_FEATURED)

    def getLink(self,webElement:WebElement):
        return webElement.find_element_by_tag_name('a').get_attribute("href")

       
    def getElements(self,webDriver):
       return webDriver.find_elements(By.CLASS_NAME,'entry-title')
       
    def extract_paragraphs(self,webDriver:WebDriver,article_id:int)-> ParagraphsDTO:

        paragraphs = webDriver.find_element(By.CLASS_NAME,'entry-content').find_elements(By.TAG_NAME,"p")
        paragraphsDTO = ParagraphsDTO(article_id)

        order = 0

        for paragraph in paragraphs:
            paragraphsDTO.add_paragraph(ParagraphDTO(paragraph.text,order))
            order += 1

        return paragraphsDTO


    def validate_paragraph(self, paragraph: ParagraphDTO) -> bool:
        
        if len(paragraph.paragraph) < 100:
            return False
        
        return True