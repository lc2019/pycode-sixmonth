try:
    num = int(input('enter a num: '))
    x = 1 / num
    file = open('test.txt', 'r')
    print(file.read())
    file.close()
except ValueError as e:
    print('enter not num')
except ZeroDivisionError as e:
    print('num不能为0')
except FileNotFoundError as e:
    print('file not exists')
