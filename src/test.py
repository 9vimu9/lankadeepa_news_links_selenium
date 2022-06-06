from sites.CelebrityNews import CelebrityNews
from sites.Featured import Featured
from sites.Foreign import Foreign
from sites.TopStory import TopStory
from sites.TravelNews import TravelNews

import mysql.connector
from support.database.Connection import Connection
from support.initiate.Starter import Starter


if __name__ == '__main__':

    #load essential components
    Starter.start()
    
    # news = CelebrityNews()
    # news = TravelNews()
    # news = Featured()
    # news = TopStory()
    news = Foreign()
    articles = news.getLinks()
    print((articles[0]).dic())

    
    # result = Connection.query("select database();")
    # print(result)