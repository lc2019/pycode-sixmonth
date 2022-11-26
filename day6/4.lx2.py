# 定义人
class Sol(object):
    def __init__(self, name, gun=None):
        self.name = name
        self.gun = gun

    # fire动作
    def fire(self):
        if self.gun is None:
            print('no gun')
        else:
            self.gun.shoot()


# 定义gun add_bul short
class Gun(object):
    def __init__(self, gun_type, bul_count=0):
        self.gun_type = gun_type
        self.bul_count = bul_count

    # 属性1
    def add_bul(self, count):
        self.bul_count += count

    # 属性2
    def shoot(self):
        print('fire')
        self.bul_count -= 1


m416 = Gun('m4')
m416.add_bul(10)
s = Sol('lc', m416)

while True:
    s.fire()
    if m416.bul_count <= 0:
        break
