class Phone(object):

    def call(self, num):
        print(f'calling...{num}')

    def __str__(self):
        return f'typec...'


# 继承父类的方法
class Iphone(Phone):
    def carmera(self):
        print('paizhao....')


# 子类继承父类的方法和属性可以直接使用
iphonex = Iphone()
iphonex.call('10086')
iphonex.carmera()
print(iphonex)

# 私有方法和属性子类不能继承
class Acc(object):
    def __init__(self):
        self.__money=999
        self.name='tom'

    def __show(self):
        print('this is father private')

    def display(self):
        print('this is father public')
        # 通过父类的公有方法来调
        self.__show()

class Son(Acc):
    def play(self):
        print('this is son method')


s = Son()
s.play()
s.display()