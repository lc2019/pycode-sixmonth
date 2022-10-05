# chr ord
print(ord('a'))  # 97
print(chr(65))  # A 数字对应的编码
# utf8 一个字符3个编码  gbk 1个字符2个编码

# in not in
word = 'hello'
x = input("enter a c:")
for c in word:
    if x == c:
        print("exist")
        break
else:
    print('not exist')

if x in word:
    print("exist")
else:
    print('not exist')

if word.find(x) == -1:
    print("not exist")
else:
    print("exist")
