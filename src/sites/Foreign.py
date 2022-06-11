from sites.Lankadeepa import Lankadeepa
from support.Constant import Constant



class Foreign(Lankadeepa):

    def __init__(self):
        super().__init__('https://www.lankadeepa.lk/world_news/14',Constant.MAX_PAGES_FOR_ARTICLE,Constant.ARTICLE_CATEGORY_FOREIGN)

   