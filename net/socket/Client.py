# -*- coding: UTF-8 -*-

import socket 

if __name__ == "__main__":
    s = socket.socket() 
    host = '127.0.0.1'
    port = 12345 

    s.connect((host, port))
    print s.recv(1024)
    s.close()