class Account(object):
    def __init__(self, name, balance):
        # 私有属性
        self.__name = name
        self.__balance = balance

    # get set
    def get_name(self):
        return self.__name

    def set_money(self, new_b):
        if isinstance(new_b,int):
            self.__balance += new_b
        else:
            print('type error')


    def get_money(self):
        return self.__balance

    def show_info(self):
        print(self.__name + ' have', self.__balance)


account = Account('lc', 20)
account.show_info()
print(account.get_name())
account.set_money(100)
print(account.get_money())