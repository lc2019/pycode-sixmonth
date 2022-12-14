import socket
import sys
import threading


class StaticWebServer(object):
    def __init__(self, port):
        # socket
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 端口复用 立即释放
        self.ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        # 绑定端口
        self.ss.bind(("127.0.0.1", port))
        # 最大连接数
        self.ss.listen(128)

    def start(self):
        while True:
            css, ip_port = self.ss.accept()
            print(ip_port)
            # 创建子线程
            sub_thread = threading.Thread(target=self.task, args=(css,))
            sub_thread.setDaemon(True)
            # 启动线程
            sub_thread.start()
        self.ss.close()

    # 当客户端与服务端建立链接成功后 创建子线程 子线程来处理客户端的请求 防止主线程阻塞
    # 把创建的子线程设置成守护的主线程 防止主线程无法退出
    # 方法接受当前对象
    def task(self, css):
        # 链接建立成功 最大接受数
        recv_data = css.recv(4096)

        # 判断数据是否发送完成
        if len(recv_data) == 0:
            print("browser close")
            css.close()
            return

        # 解码
        decode = recv_data.decode("gbk")
        print(decode)

        # 切分
        req_list = decode.split(" ", maxsplit=2)

        # 浏览器请求资源路径
        req_path = req_list[1]
        print(req_path)

        # 判断返回对应的html
        if req_path == "/":
            req_path = "/1.格式.html"

        try:
            # 打开指定文件
            with open("static" + req_path, "rb") as file:
                # 读取文件
                file_read = file.read()
        except Exception as e:
            #  请求资源路径不存在返回404
            res_line = "HTTP/1.1 404 not found\r\n"
            res_head = "Server: pws1.0\r\n"

            # 错误的html
            with open("static/error.html", "rb") as file:
                file_read = file.read()

            # 响应error.index的内容
            res_body = file_read

            # 响应报文拼接 line header body
            res_data = (res_line + res_head + "\r\n").encode("gbk") + res_body

            # 发送数据
            css.send(res_data)
        else:

            res_line = "HTTP/1.1 200 ok\r\n"
            res_head = "Server: pws1.0\r\n"

            # 响应体 正常的文件直接读取
            res_body = file_read

            res_data = (res_line + res_head + "\r\n").encode("gbk") + res_body
            css.send(res_data)
        finally:
            css.close()


if __name__ == '__main__':
    # 命令行
    # 判断输入
    if len(sys.argv) != 2:
        print('python3 xxx.py port')
        exit(1)

    # 判断是否是数字
    if sys.argv[1].isdigit():
        port = sys.argv[1]
        StaticWebServer(port).start()
    else:
        print('python3 xxx.py port')
