import multiprocessing
import time


def task1():
    for i in range(10):
        print('a----', i + 1)
        time.sleep(1)


def task2():
    for i in range(10):
        print('b----', i + 1)
        time.sleep(1)


if __name__ == '__main__':
    # 创建子进程对象
    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)

    # 启动子进程
    p1.start()
    p2.start()
