from project.config.mongoDB import *
from bson import ObjectId

class tag_seletor():
    def __init__(self):
        self.author = 'shiyu52524'
        self.rule = ''
        self.result_tag = ''



    def selector(self,content,bs4_selector=True,xpath_selector=False):
        if bs4_selector:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(content,'lxml')
            aim = soup.select(self.rule)
            print(aim)
            for i in aim:
                if i:
                    print(i.text)
                    result = i.text
                    return result
        # if xpath_selector:
        #
        #     selector = etree.HTML(content)
        #     aim = selector.xpath(self.rule)
        #     print(aim)
        #     return aim

    def update2mongo(self,id,data):
        dict = {}
        dict[self.result_tag] = data
        result = mycol.update_many({"_id": ObjectId(id)}, {"$set": dict})
        print(result)



    def nomal_search(self):
        for item in mycol.find():
            content = item['response']
            data = self.selector(content)
            id = item['_id']
            self.update2mongo(id,data)