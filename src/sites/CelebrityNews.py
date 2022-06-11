from sites.Saravita import Saravita
from support.Constant import Constant



class CelebrityNews(Saravita):

    def __init__(self):
        super().__init__('https://www.saaravita.lk/bollyhollywood/105',Constant.MAX_PAGES_FOR_ARTICLE,Constant.ARTICLE_CATEGORY_CELEBRITY)

   