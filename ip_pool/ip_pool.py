import random
from bs4 import BeautifulSoup
from page_catcher import Scrapy
from config.redis_config import *

class ip_pool():



    def __init__(self):
        # self.source_web = 'https://www.kuaidaili.com/free/intr/'
        self.source_web = 'https://www.xicidaili.com/wn/'
        self.header = {'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                       }
        self.scrapy_tool = Scrapy()
        self.count = 0



    def __add_ip(self):
        url = 'https://www.xicidaili.com/wn/' + str(random.randint(1, 1600)) + '/'
        response = self.scrapy_tool.get_page_index(url).text
        soup = BeautifulSoup(response, 'lxml')
        RES = soup.select('#ip_list td')
        for i in range(0, len(RES)):
            if '.' in str(RES[i].text):
                x = RES[i].text + ':' + RES[i + 1].text
                if self.__try_ip(x):
                    r3.set(self.count, x)
                    self.count+=1


    def __try_ip(self,ip):
        url = r1[random.choice(r1.keys())]
        front = 'https' if 'https' in url else 'http'
        self.proxies = {front : front+'://'+ip}
        return True if self.scrapy_tool.get_page_index(url) else False

    def __check_ip(self):