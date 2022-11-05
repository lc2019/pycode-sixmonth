# 打印奇数位上的字符串
a = 'abcdef'
b = ''
# 通过下标判断
for i, j in enumerate(a):
    if i % 2 != 0:
        b += j
print(b)
