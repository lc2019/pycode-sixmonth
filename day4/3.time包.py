import time


def js():
    x = 0
    for i in range(1, 100000):
        x += 1


# 程序花费时间函数
def hftime(fn):
    start = time.time()
    fn()
    end = time.time()
    print(end - start)


hftime(js)
