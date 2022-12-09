# 线程
import threading
import time


def task1(count):
    for i in range(count):
        print('task----', i + 1)
        time.sleep(0.5)


def task2(content, count):
    for i in range(count):
        print(content, 'task----', i + 1)
        time.sleep(0.5)


if __name__ == '__main__':
    # 1.带参数 args
    t1 = threading.Thread(target=task1, args=(5,))
    t1.start()

    # 2. kwargs 字典带方式
    t2 = threading.Thread(target=task2, kwargs={'content': 'hello', 'count': 5})
    t2.start()

    print('main over')
