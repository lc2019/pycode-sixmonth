import time


def calc_time(fn):
    print("外部函数")

    def inner():
        start = time.time()
        fn()
        end = time.time()
        print("代码耗时：", end - start)

    return inner


# 装饰器
@calc_time
# 1.调用外部函数
# 2.将被装饰的函数传递给fn
def js():
    x = 0
    for i in range(1, 100000):
        x += 1
    print(x)


# 3.讲js函数装饰进去inner
js()
