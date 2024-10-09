import datetime
from multiprocessing import Pool


def read_info(name):
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break


if __name__ == '__main__':

    filenames = ['./file 1.txt', './file 2.txt', './file 3.txt', './file 4.txt']

    start = datetime.datetime.now()
    for filename in filenames:
        read_info(filename)
    end = datetime.datetime.now()
    print(end - start)

    start = datetime.datetime.now()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)
