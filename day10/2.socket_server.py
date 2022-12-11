import socket

if __name__ == '__main__':
    # server socket
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用 让程序退出端口立即释放
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 绑定端口
    ss.bind(("", 8989))
    # 监听端口 连接数128
    ss.listen(128)

    # 等待客户端建立连接
    server_client_socket, ip_port = ss.accept()
    print('客户端的ip和端口', ip_port)

    # 接受的数据最大字节数1024
    recv_data = server_client_socket.recv(1024)
    print('接受数据的长度为： ', len(recv_data))

    # decode
    data_decode = recv_data.decode("utf-8")
    print('服务端接受的数据是： ', data_decode)

    # 与客户端交互 发送数据
    ok_encode = "ok,以及收到正在处理中。。。".encode("utf-8")
    server_client_socket.send(ok_encode)

    # 关闭与客户端连接
    server_client_socket.close()

    # 关闭与服务端连接
    ss.close()
