#!/usr/bin/python3.8

import socket
import time

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1)
message = b'test'
start = time.time()
addr = ("127.0.0.1", 1463)
clientSocket.sendto(message, addr)

#s.connect((socket.gethostname(), 1463))


while True:
    msg = clientSocket.recv(4068)
    print(msg.decode("utf-8"))
   # s.close()
