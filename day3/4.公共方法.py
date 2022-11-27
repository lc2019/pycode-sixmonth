# + 用于拼接 字符串 元组 列表
print('hello' + ' world')

# - 用于集合 求差集
print({1, 2, 3} - {3})  # {1, 2}

# 带下标的遍历  enumerate 列表和元组
nums = [1, 2, 3, 4, 5]
for i, v in enumerate(nums):
    print('第%d个数据是%d' % (i, v))
