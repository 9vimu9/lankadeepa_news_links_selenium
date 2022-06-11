from sites.Lankadeepa import Lankadeepa
from support.Constant import Constant



class Knowledge(Lankadeepa):

    def __init__(self):
        super().__init__('https://www.lankadeepa.lk/encyclopedia/17',Constant.MAX_PAGES_FOR_ARTICLE,Constant.ARTICLE_CATEGORY_KNOWLEDGE)

   