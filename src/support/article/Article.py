import string


class Article:
    
    def __init__(self,title:string,url:string,category:string,id:int=None):
        self.title = title
        self.url = url
        self.category = category
        self.id = id
    
    def dic(self):
        
        return {
            'title':self.title,
            'url':self.url,
            'category':self.category,
            'id':self.id
        }
