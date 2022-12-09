# 线程
import threading
import time


def task1():
    for i in range(5):
        print('task1----', i + 1)
        time.sleep(1)


def task2():
    for i in range(5):
        print('task2----', i + 1)
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()
    print('main over')
