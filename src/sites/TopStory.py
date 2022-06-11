from sites.Lankadeepa import Lankadeepa
from support.Constant import Constant



class TopStory(Lankadeepa):

    def __init__(self):
        super().__init__('https://www.lankadeepa.lk/top_story/10',Constant.MAX_PAGES_FOR_ARTICLE,Constant.ARTICLE_CATEGORY_NEWS)

   