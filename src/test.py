from sites.CelebrityNews import CelebrityNews
from sites.Featured import Featured
from sites.Foreign import Foreign
from sites.Knowledge import Knowledge
from sites.TopStory import TopStory
from sites.TravelNews import TravelNews
from model.Article import Article

from support.database.Connection import Connection
from support.initiate.Starter import Starter


if __name__ == '__main__':

    #load essential components
    Starter.start()
    
    # news = CelebrityNews()
    # news = TravelNews()
    # news = Featured()
    # news = TopStory()
    # news = Foreign()
    # articles = news.store_articles()
    # print((articles[0]).url)
    # article_model  = Article()
    # article_model.insert(articles[0])

    (Knowledge()).store_paragraphs(5)
    # t = Article().update_paragraphs_added_status(4516,1)
    # print(t)
    # result = Connection.query("select * from articles limit 1;")
    # print(result.description)
    # print(result[0][2])
    # (TravelNews()).store_articles()
    # (CelebrityNews()).store_articles()
    # (Knowledge()).store_articles()
    # (Foreign()).store_articles()
    # (TopStory()).store_articles()
    # (Featured()).store_articles()
  