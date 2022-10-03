import random

# names = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
# username = input('输入姓名:')
# for xm in names:
#     if username == xm:
#         print("cunz")
#         break
# else:  # 循环走完才执行
#     names.append(username)
# print(names)

# 排序
nums = [3, 1, 9, 8, 0, 7]
nums.sort()
print(nums[-1])

y = -1
for x in nums:
    if x > y:
        y = x

i = 0
index = 0
while i < len(nums) - 1:
    if nums[i] > y:
        y = nums[i]
        index = i
    i += 1
print(index, y)

# 删除空的字符串
x = ['hello', '', '', 'world', 'yes', 'ok']
word = []  # 添加到新的列表
for w in x:  # 在使用for循环的时候不用对元素进行增删操作,下标会发生越界
    if w != '':
        word.append(w)
x = word
print(x)

# 老师分配办公室
teacs = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
rooms = [[], [], []]

for t in teacs:
    room = random.choice(rooms)  # 从列表随机取一个数据
    room.append(t)
print(rooms)

for i, room in enumerate(rooms):
    print('房间%d里一共多少%d个老师' % (i, len(room)))
    for t in room:
        print(t, end='\t')
    print()
