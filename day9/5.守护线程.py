# 进程不共享全局变量，主进程会等待子进程结束
import time
import threading


def task():
    for i in range(5):
        print(i)
        time.sleep(0.5)


if __name__ == '__main__':
    # 设置守护线程方式1
    p1 = threading.Thread(target=task,daemon=True)

    # 方式2
    p2 = threading.Thread(target=task)

    # p1.start()
    p2.setDaemon(True)
    p2.start()
    time.sleep(1)
    # 在主进程借宿之前调用方法结束子进程
    # p1.terminate()

    # 主线程结束子线程不在执行
    print('main process over')
