import pymongo
import datetime
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
today = datetime.date.today()
formatted_today = today.strftime('%y%m%d')
mydb = myclient[str(formatted_today)]
mycol = mydb['Scrapy']