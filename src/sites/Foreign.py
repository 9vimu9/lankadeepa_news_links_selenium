from sites.Lankadeepa import Lankadeepa
from support.Constant import Constant
from selenium.webdriver.common.by import By
from support.Constant import Constant

from selenium.webdriver.firefox.webdriver import WebDriver

from support.paragraph.ParagraphDTO import ParagraphDTO
from support.paragraph.ParagraphsDTO import ParagraphsDTO


class Foreign(Lankadeepa):

    def __init__(self):
        super().__init__('https://www.lankadeepa.lk/world_news/14',Constant.MAX_PAGES_FOR_ARTICLE,Constant.ARTICLE_CATEGORY_FOREIGN)

    def extract_paragraphs(self,webDriver:WebDriver,article_id:int)-> ParagraphsDTO:

        paragraphs = webDriver.find_element(By.CLASS_NAME,'post-content').find_elements(By.TAG_NAME,"p")
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