import string
from model.Model import Model
from support.database.Connection import Connection


class Paragraph(Model):

    def insert(self,article_id:int,paragraph:string,order:int):
        data = {
            'article_id':article_id,
            'paragraph':paragraph,
            'order':order,
        }
        Connection.insert("paragraphs",data)
    
   

#      `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
#   `article_id` bigint(20) unsigned NOT NULL,
#   `paragraph` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
#   `order` smallint(5) unsigned NOT NULL,
#   `approved` smallint(5) unsigned NOT NULL DEFAULT '2',
#   `no_more_questions` smallint(5) unsigned NOT NULL DEFAULT '0',
#   `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
#   `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,