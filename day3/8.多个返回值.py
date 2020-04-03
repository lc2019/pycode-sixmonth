def test(a, b):
    x = a // b
    y = a % b
    return x, y


res = test(13, 5)
print(res[0], res[1])
