# 给进程传递参数args-()方式传递 kwargs-dict方式传递

# 获取进程的id
import multiprocessing
import os
import time


# def task1(count):
#     for i in range(count):
#         print('task1---->',i+1)
#         time.sleep(1)


def task2(content, count):
    for i in range(count):
        print(content, '---->', i + 1)
        time.sleep(1)


if __name__ == '__main__':
    # 创建子进程对象,利用args传递参数
    # p1 = multiprocessing.Process(target=task1,args=(5,))
    # 利用kwargs传参
    p2 = multiprocessing.Process(target=task2, kwargs={'content': 'task2', 'count': 5})

    # 启动子进程
    # p1.start()
    p2.start()
