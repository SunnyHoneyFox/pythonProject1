import datetime
from multiprocessing import Pool


def read_info(name):
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break


if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

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
