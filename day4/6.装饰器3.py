# 被装饰的函数有参数
def can_play(clock):
    def handler_action(fn):
        pass

    return handler_action


@can_play(21)
def play_game(name, game):
    print(name + 'playing...' + game)


# play_game('lc', 'dota2')
print(play_game)

def can_play(clock):
    def handless_action(fn):
        def do_action(x, y):
            if clock > 22:
                print(f'{x}..防成谜。。。{y}')
            else:
                fn(x, y)  # 就是play_game函数

        return do_action

    return handless_action


@can_play(23)  # 传递给外层clock
def play_game(name, game):  # 传递给do_action 与内部参数个数保持一致
    print(name + ' play ...' + game)


play_game('lc', 'mh')
