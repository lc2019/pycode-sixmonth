# 进程不共享全局变量，主进程会等待子进程结束
import time
import multiprocessing

c_list = []


def add_data():
    for i in range(5):
        c_list.append(i)
        print(c_list)
        time.sleep(1)


def get_data():
    print('get:', c_list)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=add_data)
    p2 = multiprocessing.Process(target=get_data)

    p1.start()
    # 当前进程会等待p1执行完成后在继续执行
    p1.join()
    p2.start()

    print('main:',c_list)
