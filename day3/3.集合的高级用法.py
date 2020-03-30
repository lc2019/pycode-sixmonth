s1 = {'zhangsan', 'wangwu', 'zhaoliu', 'leichao', 'lisi'}
s2 = {'zhangsan', 'lisi', 'liuneng', 'zhaosi'}

# set 支持算术运算
print(s1 - s2)  # s1 和s2的差集
print(s2 - s1)  # s1 s1的差集
print(s1 & s2)  # s1 s2 的交集
print(s1 | s2)  # s1 s2的并集
print(s1 ^ s2)  # s1 s2的并集 - 交集
# {'liuneng', 'zhaosi', 'zhaoliu', 'wangwu', 'leichao'}
