from model.Model import Model
from support.article.Article import Article as ArticleDTO
from support.database.Connection import Connection


class Article(Model):

    def insert(self,article:ArticleDTO):
        Connection.insert("articles",article.dic())
    
    def get_fresh_article(self,category:int):
        query = "SELECT id,title,url,category FROM articles WHERE paragraphs_added = 0 AND category = "+str(category)+" LIMIT 1";
        article = (Connection.query(query))[0]
        return ArticleDTO(article[1],article[2],article[3],article[0])
    
    def find(self,id:int):
        query = "SELECT id,title,url,category FROM articles WHERE id = "+str(id)+" LIMIT 1";
        article = (Connection.query(query))[0]
        return ArticleDTO(article[1],article[2],article[3],article[0])
