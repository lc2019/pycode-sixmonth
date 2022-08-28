# 统计100以内个位数是2并且能被3整除的数的个数下
for i in range(1, 111):
    if i // 10 == 2 and i % 3 == 0:
        print(i)

# 判断一个整数是几位数1234567
count = 0
num = int(input("enter a num:"))
while True:
    count += 1
    num //= 10
    if num == 0:
        break
print(count)

# 水仙花数
for i in range(100, 1000):
    g = i % 10
    s = i // 10 % 10
    b = i // 100
    if g ** 3 + s ** 3 + b ** 3 == i:
        print(i)

# 质数
for i in range(101, 201):
    for j in range(2, i):  # 因数
        if i % j == 0:
            break  # 如果有其他因数直接结束
    else:  # 循环外
        print(i)

# 假设
for i in range(101, 201):
    flag = True  # 每次假设i是一个质数
    for j in range(2, i):
        if i % j == 0:  # 如果i有因数说明他不是质数
            flag = False
            break
    if flag:
        print(i)

# 计数
for i in range(101, 201):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count == 0:  # 说明i没有有因数
        print(i)

# 斐波那契数列 1 1 2 3 5
num1 = 1
num2 = 1
for i in range(0, 10):
    a = num1
    num1 = num2
    num2 = a + num2
    print(num1, num2)

# 百马百担 大马3 中马2 2小马1 100马100担 大马x 中马 y 小马100 -x-y
for x in range(0, 100 // 3 + 1):
    for y in range(0, 100 // 2 + 1):
        if 3 * x + 2 * y + (100 - x - y) * 0.5 == 100:
            print(x, y, (100 - x - y))

# 纸片折叠
height = 0.08 / 1000
count = 0
while True:
    height *= 2  # 对折
    count += 1
    if height >= 8848.3:
        break
print(count)
