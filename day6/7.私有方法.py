class Thd(object):
    def __init__(self):
        self.__list = []

    def add_task(self, url):
        self.__list.append(url)
        # 通过公有的方法调用私有方法
        self.__download_date(url)

    # 私有方法
    def __download_date(self, url):
        print(f'url is downing ...{url}')


th = Thd()
th.add_task('http://baidu.com/a.mp4')
