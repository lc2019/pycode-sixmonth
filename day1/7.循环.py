print('hello world' "\n" * 2)

# while for
# while 判断条件
# 条件成立执行代码
x = 0
while x < 2:
    print('hello')
    x = x + 1

sum = 0
i = 0
# while i <10:
#     i +=1
#     sum +=i
# print(sum)

while i < 10:
    i += 1
    # 加入判断条件
    if i % 2 == 0:
        sum += i
print(sum)

# for in 后面是可迭代对象（字符串 列表 元祖 range 集合）
for i in range(1, 5):  # range 左闭右开
    print(i)

for x in 'hello':
    print(x, "\n", end='')

for i in range(1, 5):
    if i == 3:
        continue
    print(i)

# while True:
#     username = input("用户名：")
#     password = input('mima:')
#     if username =='zhangsan' and password =='123':
#         break

# while
num = 0
total = 0
count = 0
while num != 'pc':
    total += int(num)  # 先执行
    num = input('enter a num:')
    if num == 'pc':  # 不计算次数
        break
    count += 1
print(total / count)
