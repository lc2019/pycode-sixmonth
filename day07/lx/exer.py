import random


class Exerc(object):
    '''
    统计列表中的元素出现次数,按升序排序输出
    '''

    @staticmethod
    def exer1():
        # 保存数据的列表
        c_list = [1, 1, 2, 4, 4, 6, 7, 3, 2, 2, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 4, 5, 77, 3, 3, 3, 22, 1]
        new_list = []

        # 将数据去重
        c_set = set(c_list)
        # 遍历去重后的数据
        for n in c_set:
            # 对去重后的数据,在原列表中进行统计
            new_list.append({n: c_list.count(n)})

        # 生成一个字典加到新列表中
        new_list.sort(key=lambda d: list(d.values())[0])
        # 对新列表按次数进行排序输出
        print(new_list)

        # [{'1':2},{'2':3},{'4': 10}]

        '''
            有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
            123
            124
            234
            231
        '''

    @staticmethod
    def exer2():
        # 三重循环
        for i in range(1, 5):
            for j in range(1, 5):
                for k in range(1, 5):
                    # 判断无重复
                    if i != j and j != k and i != k:
                        print(i, j, k)
                        print(i * 100 + j * 10 + k)

    '''
    求出100以内的所有素数
    素数: 只能被1和本身除尽的数 (1,n)  
    '''

    @staticmethod
    def exer3():
        for i in range(1, 101):
            for j in range(2, i / 2):
                if i % j == 0:
                    break
            else:
                print(i)

    '''
    求出所有三位数中的水仙花数
      水仙花数: 一个三位数,每一位的立方累加和等于该数本身 153 = 1 + 125 + 27
    '''

    @staticmethod
    def exer4():
        # 遍历 所有的三位数
        for i in range(100, 1000):
            # 分解每个位
            a = i // 100
            b = i % 100 // 10
            c = i % 10

            # 判断 立方和是否等该本身
            if i == (a ** 3 + b ** 3 + c ** 3):
                print(i)

    '''
       输入若干数字,当输入quit时退出输入,计算输入数字中的最大值,最小值,总和,平均值
       '''

    @staticmethod
    def exer5():
        # 定义一个用来计数的变量
        n = 0
        sum = 0

        while True:
            # 输入一个数据
            data = input('请输入一个数字:')
            # 判断是否可法
            if data.isdigit():
                # 改变计数器
                n += 1
                m = int(data)
                sum += m
                if n == 1:
                    max = m
                    min = m
                else:
                    if m > max:
                        max = m
                    if m < min:
                        min = m
            else:
                if data == 'quit':
                    break
                else:
                    print('输入非法字符,重新输入')

        print('Max: ', max)
        print('Min: ', min)
        print('Sum: ', sum)
        print('Avg: ', sum / n)

    '''
    循环输入若干次字符,输入quit时退出,统计数字,字母,空白,其它字符各有多少(一次只允许输入一个字符)
    '''

    @staticmethod
    def exer6():
        number = 0
        alpha = 0
        space = 0
        other = 0

        while True:
            data = input('请输入字符')
            # 判断是否退出
            if data == 'quit':
                break
            else:
                if len(data) > 1:
                    # 将输入的字符串切出来第一个字符
                    data = data[:1]
                # 判断
                if data.isdigit():
                    number += 1
                elif data.isalpha():
                    alpha += 1
                elif data.isspace():
                    space += 1
                else:
                    other += 1
        print('number: ', number)
        print('alpha :', alpha)
        print('space :', space)
        print('other :', other)
        print('total :', number + alpha + space + other)

    '''
    输入两个数字 a, b 求s=a+aa+aaa+aaaa+aa...a的值
    例如输入 2, 5
    输出结果 2+22+222+2222+22222 = 24690(此时共有5个数相加)
    输出格式为: x+xx+xx+xx=xxxxx 形式

    '''

    @staticmethod
    def exer7():
        a = int(input('A:'))
        b = int(input('B:'))

        i = 1
        s = 0
        sum = 0
        n_s = ''
        while i <= b:
            s = s * 10 + a
            if i != b:
                n_s += str(s) + '+'
            else:
                n_s += str(s) + '='
            # 数字的结果
            sum += s
            i += 1
        # 字符串拼接
        n_s += str(sum)
        print(n_s)

    '''
    现有 姓氏 和 名字 若干
    设计函数得到一个随机的名字
    '''

    @staticmethod
    def exer8():
        # 定义两个列表用来保姓和名
        last_name = ['张', '王', '李', '赵', '周', '吴', '郑', '钱', '上官', '欧阳', '诸葛', '南宫', '东方']
        first_name = ['健强', '波', '建国', '建军', '国庆', '超群', '传', '鹏', '狗蛋', '不败']

        # 利用随机值,分别获取一个值进行拼接
        ln_index = random.randint(0, len(last_name) - 1)
        fn_index = random.randint(0, len(first_name) - 1)

        name = last_name[ln_index] + first_name[fn_index]
        print(name)

    '''
    利用随机数得到一个随机的字母和数字组成的四位验证码
    然后输入看到的验证码,如果输入正确结束程序,输入错误持续输入直到正确为止

    (进阶(作业):如果输入三次不正确,更换验证码后继续)
    '''

    @staticmethod
    def exer9():
        '''
         0-9: 48 - 57
         A - Z: 65 - 90
         a - z: 97 - 122

        '''

        print('\a')

        # 要一个四位数
        i = 1
        v_code = ''
        while i <= 4:
            n = random.randint(48, 122)

            if (n >= 48 and n <= 57) or (n >= 65 and n <= 90) or (n >= 97 and n <= 122):
                v_code += chr(n)
                i += 1

        print(v_code)

        # 持续输入并判断
        while True:
            inpu_data = input('请输入:')
            if inpu_data == v_code:
                print('验证成功')
                break
            else:
                print('输入错误,重新输入')

    '''
    求出所有字符串的最小前缀
    a
    ab
    abbc
    abc
    abd
    d 

    '''

    @staticmethod
    def exer10():
        str_list = ['abc', 'ab', 'abc', 'abcd', 'abd', 'ad']

        '''
        ab      ab

        ab      ab
        abc     ab
        abc     ab
        abd     ab
        abcd    ab


        '''

        # 对列表中的字符串按长度进行排序,找到最短串
        str_list.sort(key=lambda s: len(s))
        # 找到最短字符串
        short_s = str_list[0]

        # 对所有的字符串进行比较,如果有一个不同,说明该字符前的字符串就是最短串
        for i in range(0, len(short_s)):
            # 遍历列表中的所有字符串
            for s in str_list:
                # 判断最短串的第i个字符是否和任意一个字符串的第i个字符相同
                # 如果相同,继续比较,如果不同,切片
                if short_s[i] != s[i]:
                    return short_s[:i]

        # 如果循环执行完毕都没有结束,那么说最短串就是最小前缀
        # return short_s
        print(short_s)

    '''
    按从高到低的顺序统计文章text中所有单词的使用频率
    '''

    @staticmethod
    def exer11():
        new_list = []
        # 打开文件
        file_r = open('text', 'r')

        # 读取文件内容
        content = file_r.read()
        file_r.close()

        # 分割文件内容
        word_list = content.split()

        # 对分割后字符串元素进行去重
        word_set = set(word_list)

        # 遍历
        for s in word_set:
            # 统计,并组合成字典, 放到新列表
            n = word_list.count(s)
            new_list.append({s: n})

        # 对新列表进行排序显示
        new_list.sort(key=lambda d: list(d.values())[0], reverse=True)

        print(new_list)
        # return new_list
