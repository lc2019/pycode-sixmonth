import socket


def main():
    # socket
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口复用 立即释放
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 绑定端口
    ss.bind(("127.0.0.1", 9000))
    # 最大连接数
    ss.listen(128)

    while True:
        # 等待接受客户端的链接
        css, ip_port = ss.accept()

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
    main()
