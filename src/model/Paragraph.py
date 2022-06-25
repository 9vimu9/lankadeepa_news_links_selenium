import string
from typing import Union
from model.Article import Article
from model.Model import Model
from support.Constant import Constant
from support.Slack.ParagraphSaved import ParagraphSaved
from support.database.Connection import Connection
from support.paragraph.ParagraphDTO import ParagraphDTO


class Paragraph(Model):

    def insert(self,article_id:int,paragraph:string,order:int):
        data = {
            'article_id':article_id,
            'paragraph':paragraph,
            'order':order,
        }
        print(data)
        last_id = Connection.insert("paragraphs",data)
        if not last_id:
            raise Exception("paragraph save failed")
        paragraph = self.find(last_id)

        if not paragraph:
            raise Exception("paragraph save failed")
        
        ParagraphSaved(paragraph).send()
        Article().update_paragraphs_added_status(paragraph.article_id,Constant.ALL_THE_ARTICLE_PARAGRAPHS_ADDED)
        return paragraph
        
    
    def find(self,id:int)-> Union[ParagraphDTO,bool]:
        query = "SELECT id,article_id,paragraph,`order` FROM paragraphs WHERE id = "+str(id)+" LIMIT 1";
        paragraph = Connection.query(query)
        if not paragraph:
            return False
        return ParagraphDTO(paragraph[0][2],paragraph[0][3],paragraph[0][1],paragraph[0][0])


#      `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
#   `article_id` bigint(20) unsigned NOT NULL,
#   `paragraph` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
#   `order` smallint(5) unsigned NOT NULL,
#   `approved` smallint(5) unsigned NOT NULL DEFAULT '2',
#   `no_more_questions` smallint(5) unsigned NOT NULL DEFAULT '0',
#   `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
#   `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,