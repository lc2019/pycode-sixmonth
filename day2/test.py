num1 = 1
num2 = 1
for i in range(0, 10):
    a = num1
    num1 = num2
    num2 = a + num2
    print(num1, num2)
