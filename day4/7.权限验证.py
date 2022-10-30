# 函数实例 权限验证
# 权限因子
READ_PER = 4
WRITE_PER = 2
EXEC_PER = 1
# 用户权限
user_per = 3


def check_per(base_per):
    def hand_action(fn):
        # 扩展功能
        def do_action():
            if user_per & base_per != 0:
                fn()
            else:
                print("no permit...")

        return do_action

    # 装饰函数
    return hand_action


@check_per(READ_PER)
def read():
    print('read....')


read()
