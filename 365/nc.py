#!/usr/bin/python3.8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1857))

while True:
    msg = s.recv(4068)
    print(msg.decode("utf-8"))
   # s.close()
