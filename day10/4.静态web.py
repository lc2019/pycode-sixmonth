import socket

if __name__ == '__main__':
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

    ss.bind(("127.0.0.1",9000))
    ss.listen(128)

    while True:
        css,ip_port = ss.accept()
        recv_data = css.recv(4096)
        decode = recv_data.decode("gbk")
        print(decode)

        with open("static/index.html","rb") as file:
            file_read = file.read()
        # 相应代码
        res_line = "HTTP/1.1 200 ok\r\n"
        res_head = "Server: pws1.0\r\n"
        # index的内容
        res_body = file_read


        res_data = (res_line+res_head+"\r\n").encode("gbk")+res_body

        css.send(res_data)

        css.close()
