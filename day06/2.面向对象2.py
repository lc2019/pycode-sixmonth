# 烤地瓜

class dg(object):
    # 初始化状态和时间
    def __init__(self):
        self.status = '生gua蛋子'
        self.total_time = 0

        #调料
        self.condi=[]

    # 烤地瓜的方法
    def cook(self, t):
        self.total_time += t

        if self.total_time < 3:
            self.status = '生gua蛋子'
        elif self.total_time < 6:
            self.status = '半生不熟'
        elif self.total_time < 8:
            self.status = '刚刚好'
        elif self.total_time < 10:
            self.status = '烤糊了'
        else:
            print('不能吃了')

    def add_cond(self,t1):
        self.condi.append(t1)

    def __str__(self):

        s = f'{self.status} 烤了 {self.total_time} min'
        for i in self.condi:
            s +=(i+'\n')

        return s



d1 = dg()
print(d1)
d1.cook(8)
d1.add_cond('蜂蜜')
d1.add_cond('奶油')
print(d1)
