nums = [i for i in range(10)]
print(nums)

x = [i for i in range(10) if i % 2]  # 0 表示False 其他 表示True
print(x)

m = [i for i in range(1, 101)]
# 使用切片来解决
n = [m[j:j + 3] for j in range(0, 100, 3)]
print(n)
