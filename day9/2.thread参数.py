# 线程
import threading
import time


def task1():
    # 获取当前线程对象
    t = threading.current_thread()
    print('task-1',t.name)
    for i in range(5):
        print('task1----', i + 1)
        time.sleep(1)


def task2():
    t = threading.current_thread()
    print('task-2',t.name)
    for i in range(5):
        print('task2----', i + 1)
        time.sleep(1)


if __name__ == '__main__':
    t = threading.current_thread()
    print('main',t.name)
    t1 = threading.Thread(target=task1,name='t1')
    t2 = threading.Thread(target=task2,name='t2')

    t1.start()
    t2.start()
    print('main over')

    print(t1,t2)
