# 线程共享全局变量

import threading
import time

c_list = []


def add_data():
    for i in range(5):
        c_list.append(i)
        print(c_list)
        time.sleep(0.5)


def read_data():
    print('read...', c_list)


if __name__ == '__main__':
    add_t = threading.Thread(target=add_data)
    read_t = threading.Thread(target=read_data)

    add_t.start()
    # 线程执行顺序无法控制，等待add完成后在继续往下执行，阻塞
    add_t.join()
    read_t.start()
