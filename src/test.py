from sites.CelebrityNews import CelebrityNews
from sites.Featured import Featured
from sites.Foreign import Foreign
from sites.TopStory import TopStory
from sites.TravelNews import TravelNews


if __name__ == '__main__':
    
    # news = CelebrityNews()
    # news = TravelNews()
    # news = Featured()
    # news = TopStory()
    news = Foreign()
    print(news.getLinks())