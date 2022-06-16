from model.Model import Model
from support.article import Article
from support.database.Connection import Connection


class Article(Model):

    def insert(self,article:Article):
        Connection.insert("articles",article.dic())
     