# 等待锁的释放
import threading
import time

lock = threading.Lock()


# 根据下标取值 保证同一时刻只有一个线程取值
def get_value(index):
    # 上锁
    lock.acquire()
    print(threading.current_thread())
    my_list = [1, 2, 3, 5]
    # 判断下标是否越界
    if index >= len(my_list):
        print('下标越界:', index)
        # return 一旦越界无法释放锁，造成死锁，应该在越界之前释放锁
        lock.release()
        return
    value = my_list[index]
    print(value)
    time.sleep(0.2)

    # 释放锁
    lock.release()


if __name__ == '__main__':
    for i in range(30):
        t = threading.Thread(target=get_value, args=(4,))
        t.start()

    print('main over')
