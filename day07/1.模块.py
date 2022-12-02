# 导入模块
import os

print(os.listdir())
# 别名
import datetime as dt

print(dt.datetime.now())
# 从模块导入包
from random import randint

print(randint(10, 20))

from random import randrange as rr

print(rr(20, 30))
