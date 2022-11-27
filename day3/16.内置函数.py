# 内置函数总结

# all转行为bool值 全为true则true，否则为false
print(all(['hello', 0]))

# 列出所有的方法
print(dir(list))

nums = [1, 3, 5, 7]


def test(e):
    return e * 2


# 可迭代对象，可以将他转为列表
x = map(test, nums)
print(list(x))
