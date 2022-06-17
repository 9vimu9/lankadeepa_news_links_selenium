import string

from support.Constant import Constant


class ParagraphDTO:
    
    def __init__(self,paragraph:string,order:int,no_more_questions:int=Constant.PARAGRAPH_CAN_CREATE_QUESTIONS):
        self.paragraph = paragraph
        self.order = order
        self.no_more_questions = no_more_questions
    
    def dic(self):
        
        return {
            'paragraph':self.article_id,
            'order':self.order,
            'no_more_questions':self.no_more_questions,
        }

