nums = [1, 4, 2, 3]  # 列表
nums.sort()  # 直接对列表进行排序
print(nums)


def fx(x):
    return x ** 2


# nums2 = map(fx, nums)
nums2 = map(lambda n : n**2, nums)
for i  in nums2:
    print(i)

# 内置函数不会改变原有的数据，生成新的结果
res = sorted(nums)
print(res)

stu = [
    {'name': 'lc', 'age': 18},
    {'name': 'll', 'age': 19}
]

# def foo(stu):
#     return stu['age']  # 通过返回值告诉sort按照属性排序

# 按照指定的元素进行排序，使用key设置比较规则--sort进阶用法
stu.sort(key=lambda stu: stu['age'])

print(stu)
