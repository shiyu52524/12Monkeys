from project.multiprogress_handler import mutiprogress
from project.read2redis import read_data
from project.response_handler import tag_seletor

if __name__ == '__main__':
    read = read_data()
    read.path = r"..\docs\test.csv"
    read.read_csv()



    mult= mutiprogress()
    mult.core = 8
    mult.MonkeyKing()
    tool = tag_seletor()



    tool.rule = '#pro_info_1  tr:nth-child(1) td p'
    tool.result_tag = 'result1'
    tool.nomal_search()