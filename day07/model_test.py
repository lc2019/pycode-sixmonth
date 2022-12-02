a = 10


def test():
    print('testting...')


class Person(object):
    def eat(self):
        print('eatting...')


p = Person()
eat = p.eat


def add(x, y):
    return x + y


# 直接执行当前py文件 __name__的值是__main__
if __name__ == '__main__':
    m = add(2, 3)
    print('代码执行了')
    print(m)
