import csv
from project.config.redis import *

class read_data:

    def __init__(self):
        self.path = ""

    def read_csv(self):
        r1.flushdb()
        r2.flushdb()
        with open(self.path, 'rt', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
                key = "%s"%row[0]
                url = "%s"%row[1]
                r1.set(key,url)