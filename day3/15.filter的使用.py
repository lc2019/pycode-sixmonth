from functools import reduce

# filter进行过滤 对可迭代对象进行过滤 得到一个filter对象
ages = [19, 18, 29, 28, 30]
# filter(function or None, iterable)
x = filter(lambda ele: ele > 18, ages)
print(x)  # <filter object at 0x10f803668> 得到可迭代对象
print(list(x))
for a in x:
    print(a)

scores = [100, 98, 99, 80, 60]
print(reduce(lambda ele1, ele2: ele1 + ele2, scores))

stu = [
    {'name': 'lc', 'age': 18},
    {'name': 'll', 'age': 19},
    {'name': 'llu', 'age': 17},
    {'name': 'lcc', 'age': 29},
]


def bar(x, y):
    return x + y['age']


# 12叠加 在跟3加

# reduce(function, sequence, initial=None)
print(reduce(bar, stu, 0))
