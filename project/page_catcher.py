from __future__ import division
from requests import get
from time import sleep
import random
from project.conf_redis import *
from project.conf_mongo import *
import json
mycol = mydb['Scrapy']



class page_cather():


    def __init__(self):

        user_agent = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]
        self.cookie = ''
        self.header = {'User-Agent': random.choice(user_agent),
                       'Cookie':self.cookie
                       }
        self.proxies = {}
        self.json_parser = False


    def get_page_index(self,url):
        i=0
        while i<3:
            try:
                response = get(url=url,
                               headers=self.header,
                               allow_redirects=False,
                               proxies=self.proxies,
                               timeout=(5,10))
                if response.status_code == 200:
                    return response
                elif response.status_code == 301 or 302:
                    new_url = response.headers['Location']
                    print('发生重定向,新请求地址为'+new_url)
                    self.get_page_index(new_url)
                elif response.status_code== 429:
                    print('监听到访问限制，等待时间%s秒'%response.headers['Retry-After'])
                    sleep(response.headers['Retry-After']+1)
                    self.get_page_index(url)
                elif response.status_code == 404:
                    print('此页面不存在')
                    return None
                else:
                    print('http error'+response.status_code)
                    return None
            except:
                i+=1
                print('other error,retry %s time'%i)



    def catch_content(self,key,url):
        response = self.get_page_index(url)
        content = json.loads(response) if self.json_parser else response.text
        if content is not None:
            mydict = {'key': key,
                      'url': url,
                      'response': content
                      }
            mycol.insert_one(mydict)
            r1.delete(key)

        else:
            r1.delete(key)
            r2.set(key, url)
        a = 1 - len(r1.keys()) / l
        percentage = "%.3f%%" % (a * 100)
        print(percentage)

