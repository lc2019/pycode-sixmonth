# chr ord
print(ord('a'))  # 97
print(chr(65))  # A 数字对应的编码
# utf8 一个字符3个编码  gbk 1个字符2个编码

# in not in
word = 'hello'
x = input("enter a c:")
for c in word:
    if x == c:
        print("cunz")
        break
else:
    print('bucunz')

if x in word:
    print("cunz")
else:
    print('bu cunz')
