# -*- coding: UTF-8 -*-
import socket
print help(socket.socket.accept)

if __name__ == "__main__":
    s = socket.socket()
    host = '127.0.0.1'
    print host

    port = 12345
    s.bind((host, port))

    s.listen(5)
    while True:
        c, addr = s.accept()
        print help(socket.accept)
    	print '连接地址：', addr
        c.send('欢迎访问菜鸟教程！')
        c.close()