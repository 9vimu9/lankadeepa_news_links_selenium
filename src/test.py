from sites.CelebrityNews import CelebrityNews
from sites.Featured import Featured
from sites.Foreign import Foreign
from sites.TopStory import TopStory
from sites.TravelNews import TravelNews

import mysql.connector
from support.database.Connection import Connection


if __name__ == '__main__':
    
    # news = CelebrityNews()
    # news = TravelNews()
    # news = Featured()
    # news = TopStory()
    news = Foreign()
    # print(news.getLinks())

    
    # conn = mysql.connector.connect(host = 'mydb', user = 'root', password = 'root', port = 3306)

    # cursor = conn.cursor()
    # databases = ("show databases")
    # cursor.execute(databases)
    # for (databases) in cursor:
    #     print (databases[0])

    result = Connection.query("select database();")
    print(result)
