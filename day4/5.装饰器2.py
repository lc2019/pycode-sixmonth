# 带参数的装饰器

def can_play(fn):
    def inner(x, y, *args, **kwargs):
        clock = args[0]
        if clock > 21:
            print("防成谜。。。")
        else:
            fn(x, y)

    return inner


@can_play
def play_game(name, game):
    print(f'{name} play ...{game}')


play_game('lc', 'mh', 12)
