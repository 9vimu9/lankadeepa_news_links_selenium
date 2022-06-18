import string

from support.Constant import Constant


class ParagraphDTO:
    
    def __init__(
        self,
        paragraph:string,
        order:int,
        article_id:int=None,
        id:int=None,
        no_more_questions:int=Constant.PARAGRAPH_CAN_CREATE_QUESTIONS
        ):
        self.article_id = article_id
        self.paragraph = paragraph
        self.order = order
        self.no_more_questions = no_more_questions
        self.id = id
    
    def dic(self):
        
        return {
            'article_id':self.article_id,
            'paragraph':self.paragraph,
            'order':self.order,
            'no_more_questions':self.no_more_questions,
            'id':self.id,
        }

