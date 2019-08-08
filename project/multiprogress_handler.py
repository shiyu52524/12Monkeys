from multiprocessing import Pool
from project.conf_redis import *
from project.page_catcher import page_cather



class mutiprogress():

    def __init__(self):
        self.core = 8


    def MonkeyKing(self):
        cather = page_cather()
        pool = Pool(processes=8)
        for key in r1.keys():
            pool.apply_async(cather.catch_content, (key, r1[key],))
        pool.close()
        pool.join()