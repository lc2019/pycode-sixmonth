# tcp开发流程
# server
"""
socket() 创建套接字
bind() 绑定短款
listen() 设置监听
accept() 等待客户端接受连接

recv() 接收数据
send() 发送数据

close() 关闭套接字
"""

# client
"""
socket() 创建套接字
connect() 和服务端建立连接
send() 发送数据
recv() 接收数据
close 关闭客户端套接字
"""
import socket

if __name__ == '__main__':
    # socket
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接server
    cs.connect(("", 8989))

    # 与server交互 发送数据 编码
    ok_encode = "你好server，我是client。。。".encode("utf-8")
    cs.send(ok_encode)

    # 接受服务端数据
    recv_data = cs.recv(1024)
    print(recv_data)
    # 数据解码
    recv_data_decode = recv_data.decode("utf-8")
    print('接受的数据是： ', recv_data_decode)

    cs.close()
