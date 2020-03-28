# age = input("enter a age:")
age = '17'
if eval(age)<18:
    print("不能进入")
else:
    print("go on")

# # 闰年
# year = int(input("enter a year: "))
year = 2005
if (year % 4 ==0 and year % 100 !=0) or (year % 400 ==0):
    print("runnian")


# 时间
#3718 - 3600 118 /60
x = 3718
hour = x //3600
min = x % 3600 // 60
sec = x % 60
print(hour,min,sec)

#if的判断逻辑
# score = int(input("enter a score:"))
score = 78
if 60 > score >=0:
    print("too hard")
elif 80 > score >=60:
    print("yibanban")
elif 90 > score >=80:
    print('good')
elif 100 >= score >=90:
    print("youxiu")


# 嵌套if
ticket = input("买票了没 y/n:")
if ticket =='y':
    print('mai票了')
    safe = input("anjian?y/n")
    if safe =='y':
        print('jinzhan')
    else:
        print("jinzhan mei anjian")
else:
    print("mei maipaio")

# pass 使用
age = 19
if age>18:
    pass #没有意义 至少保证程序的完整性 占位、、、
print('hello')


#三元表达式
num1 =20
num2 =30
# if num1 > num2 - num1 否则num2
x  =  num1 if num1 > num2 else num2
print('大的数是：',x)