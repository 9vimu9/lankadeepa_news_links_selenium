from sites.Saravita import Saravita
from support.Constant import Constant
from selenium.webdriver.common.by import By
from support.paragraph.ParagraphDTO import ParagraphDTO
from support.paragraph.ParagraphsDTO import ParagraphsDTO
from selenium.webdriver.firefox.webdriver import WebDriver


class TravelNews(Saravita):

    def __init__(self):
        super().__init__('https://www.saaravita.lk/travel/110',Constant.MAX_PAGES_FOR_ARTICLE,Constant.ARTICLE_CATEGORY_TRAVEL)

    def extract_paragraphs(self,webDriver:WebDriver,article_id:int)-> ParagraphsDTO:

        paragraphs = webDriver.find_element(By.TAG_NAME,'article').find_elements(By.TAG_NAME,"p")
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