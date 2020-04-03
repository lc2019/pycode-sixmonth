def test():
    print('test')
    demo()


def demo():
    print('demo')


test()

count = 0


def tell_story():
    global count
    count += 1
    print('hello')
    if count <= 4:
        tell_story()  # 递归，自己调用自己


tell_story()


def get_sum(n):
    sum = 0
    if n == 0:
        return 0
    return n + get_sum(n - 1)


print(get_sum(5))


def fac(n):
    if n == 0:
        return 1
    return n * fac(n - 1)


print(fac(5))


def fbnq(n):
    # 1,1,2,3,5,8,13,21,34
    if n == 1 or n == 2:
        return 1
    return fbnq(n - 2) + fbnq(n - 1)


print(fbnq(8))
