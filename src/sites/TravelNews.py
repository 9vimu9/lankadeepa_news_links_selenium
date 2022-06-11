from sites.Saravita import Saravita
from support.Constant import Constant



class TravelNews(Saravita):

    def __init__(self):
        super().__init__('https://www.saaravita.lk/travel/110',Constant.MAX_PAGES_FOR_ARTICLE,Constant.ARTICLE_CATEGORY_TRAVEL)
