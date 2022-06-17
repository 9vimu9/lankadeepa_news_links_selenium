import string

from model.Article import Article
from support.paragraph.ParagraphDTO import ParagraphDTO

class ParagraphsDTO:
    
    def __init__(self,article_id:int):
        self.article_id = article_id
        self.article = Article().find(article_id)
        self.paragraphs = []


    def add_paragraph(self,paragraph:ParagraphDTO):
        self.paragraphs.append(paragraph)
    
    
    def dic(self):
        
        return {
            'article':self.article,
            'paragraphs':self.paragraphs,
        }

