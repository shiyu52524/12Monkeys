from multiprocessing import Pool
from config.redis_config import *
from page_catcher import page_cather



class mutiprogress():

    def __init__(self):
        self.core = 8


    def Diablo(self):
        cather = page_cather()
        pool = Pool(processes=self.core)
        for key in r1.keys():
            pool.apply_async(cather.catch_content, (key, r1[key],))
        pool.close()
        pool.join()