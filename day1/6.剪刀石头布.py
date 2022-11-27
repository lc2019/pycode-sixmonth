import random

palyer = int(input('请输入 0 剪刀 1石头 2布 ：'))
print('enter a num', palyer)

rand = random.randint(0, 2)
print('pc enter', rand)

# 赢的规则
if (palyer == 0 and rand == 2) or (palyer == 1 and rand == 0) or (palyer == 2 and rand == 1):
    print('ni win')
elif palyer == rand:
    print('pingju')
else:
    print('ni shu le')
