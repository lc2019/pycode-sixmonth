# true 的时候执行
4 > 3 and print("hello world")

# 取第一个false的值，所有未true去最后1个值
print(3 and 5 and 0 and 'hello')  # 0
# 取第一个为true取最后1个
print(0 or [] or '5' or 'ok')  # 5
