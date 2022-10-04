num = [6, 5, 3, 1, 8, 7, 2, 4]
i = 0
while i < len(num) - 1:
    n = 0
    flag = True
    # 比较过的不需要再次进行比较
    while n < len(num) - 1 - i:
        if num[n] > num[n + 1]:
            flag = False
            num[n], num[n + 1] = num[n + 1], num[n]
        n += 1
    if flag:  # 如果顺序全是对的
        break
    i += 1
print(num)

num = [6, 5, 3, 1, 8, 7, 2, 4]
num.sort()  # 排序
num.sort(reverse=True)  # 逆序
print(num)
#
# # 生成一个新的列表
x = sorted(num)
print(x)

# 直接讲列表倒叙
num.reverse()
print(num)
