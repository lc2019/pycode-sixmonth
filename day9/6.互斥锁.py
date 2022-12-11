import threading
import time

metax_lock= threading.Lock()
sum = 0


def add_sum():
    global sum
    # 对操作的变量进行枷锁
    metax_lock.acquire()
    for i in range(1000000):
        sum += 1
    # 解锁
    metax_lock.release()

    t = threading.current_thread()
    print(f'{t.name}的计算结果是{sum}')


if __name__ == '__main__':
    t1 = threading.Thread(target=add_sum)
    t2 = threading.Thread(target=add_sum)

    t1.start()
    # 线程精致导致结果错误，解决办法 线程同步
    # t1.join()
    # 互斥锁 保证同一时间只有1个线程执行
    t2.start()

    time.sleep(3)
    print('main: ', sum)
