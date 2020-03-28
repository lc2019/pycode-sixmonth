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
for i in range (100,1000):
    g = i % 10
    s = i // 10 % 10
    b = i // 100
    if g ** 3 + s ** 3 + b ** 3 == i:
      print(i)
