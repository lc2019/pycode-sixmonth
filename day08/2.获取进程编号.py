# 获取进程的id
import multiprocessing
import os
import time


def task1():
    print(f'task1的pid{os.getpid()},父进程的pid{os.getppid()}')
    time.sleep(1)


def task2():
    # 获取主进程的对象
    mp = multiprocessing.current_process()
    print('task2', mp)
    print(f'task2的pid{os.getpid()},父进程的pid{os.getppid()}')
    time.sleep(1)


if __name__ == '__main__':
    print(f'主进程的pid{os.getpid()},父进程的pid{os.getppid()}')

    # 创建子进程对象
    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)

    print(p1)
    print(p2)

    # 启动子进程
    p1.start()
    p2.start()

    print(p1)
    print(p2)
