# 进程不共享全局变量，主进程会等待子进程结束
import time
import multiprocessing


def task():
    for i in range(5):
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=task)

    p1.start()
    time.sleep(0.5)
    # 在主进程借宿之前调用方法结束子进程
    # p1.terminate()
    # 子进程守护 主进程结束了子进程仍运行
    p1.daemon = True
    print('main process over')
