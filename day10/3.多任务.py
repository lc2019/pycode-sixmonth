import socket
import threading


class SocketServer(object):
    def __init__(self):
        self.ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ser_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        self.ser_socket.bind(("", 9090))
        self.ser_socket.listen(128)

    def start(self):
        while True:
            socket_accept, ip_port = self.ser_socket.accept()
            print('链接成功', ip_port)
            thread = threading.Thread(target=self.handler_client_request, args=(socket_accept, ip_port))

            thread.setDaemon(True)
            thread.start()

        self.ser_socket.close()

    def handler_client_request(self, ss, ip_port):
        while True:
            recv_data = ss.recv(1024)
            if recv_data:
                print('接收的数据是:', recv_data.decode("gbk"), ip_port)
                ss.send('ok,正在处理中...'.encode("gbk"))
            else:
                print("client offline")
                break


if __name__ == '__main__':
    socket_server = SocketServer()
    socket_server.start()