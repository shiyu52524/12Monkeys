from __future__ import division
from multiprocessing import Pool
from page_catcher import Scrapy as tool
import datetime
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379,db  = 0)
r = redis.StrictRedis(connection_pool=pool)
keys= r.keys()
l = len(keys)

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
today=datetime.date.today()
formatted_today=today.strftime('%y%m%d')
mydb = myclient["Scrapy"+str(formatted_today)]
mycol = mydb['apexbio']



def do(key,url):
    key = bytes.decode(key)
    url = bytes.decode(url)
    web_parser = tool()
    response = web_parser.get_page_index(url).text
    if  response:
        mydict = {'key':key,
                'url':url,
                'response':response
                }
        mycol.insert_one(mydict)
        r.delete(key)
        a=1-len(r.keys())/l
        bb = "%.3f%%" % (a * 100)
        print(bb)




def main():

    pool = Pool(processes=8)
    for key in keys:
        pool.apply_async(do,(key,r[key],))
    pool.close()
    pool.join()



if __name__ == '__main__':
    main()