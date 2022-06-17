from sites.Lankadeepa import Lankadeepa
from support.Constant import Constant
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By





class Knowledge(Lankadeepa):

    def __init__(self):
        super().__init__('https://www.lankadeepa.lk/encyclopedia/17',Constant.MAX_PAGES_FOR_ARTICLE,Constant.ARTICLE_CATEGORY_KNOWLEDGE)

    
    def extract_paragraphs(self,webDriver:WebDriver):

        paragraphs = webDriver.find_element(By.CLASS_NAME,'post-content').find_elements(By.TAG_NAME,"p")
        paragraph_texts = []
        for paragraph in paragraphs:
            paragraph_texts.append(paragraph.text)

        # print(len(paragraph_texts))

        # textfile = open("a_file.txt", "w")
        # for element in paragraph_texts:
        #     textfile.write(element + "\n")
        # textfile.close()
