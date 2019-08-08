from project.multiprogress_handler import mutiprogress
from project.read2redis import read_data






if __name__ == '__main__':
    read = read_data()
    read.path = r"..\docs\test.csv"
    read.read_csv()

    mult= mutiprogress()
    mult.MonkeyKing()
