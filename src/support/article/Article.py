import string


class Article:
    
    def __init__(self,title:string,url:string,category:string):
        self.title = title
        self.url = url
        self.category = category
    
    def dic(self):
        
        return {
            'title':self.title,
            'url':self.url,
            'category':self.category,
        }
