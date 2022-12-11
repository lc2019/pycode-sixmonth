import threading
import time

sum = 0


def add_sum():
    global sum
    for i in range(1000000):
        sum += 1

    t = threading.current_thread()
    print(f'{t.name}的计算结果是{sum}')


if __name__ == '__main__':
    t1 = threading.Thread(target=add_sum)
    t2 = threading.Thread(target=add_sum)

    t1.start()
    # 线程精致导致结果错误，解决办法 线程同步
    t1.join()
    t2.start()

    print('main: ', sum)
