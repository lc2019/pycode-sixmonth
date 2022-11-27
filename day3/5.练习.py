import json

nums = [5, 2, 3, 4, 1, 8, 8, 9, 5, 3]
x = set(nums)
y = list(x)
y.sort()
print(y)

# eval json
b = '1+1'
print(eval(b))

per = {'name': 'lc', 'age': 20}  # 字典
# 字典转为json’
j = json.dumps(per)
print(j, type(j))

# json转为字典
# js = '{"name": "lc", "age": 20}'
s = json.loads(j)
print(s, type(s))
