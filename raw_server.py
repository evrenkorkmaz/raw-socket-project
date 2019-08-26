import socket
import sys
import os
s = socket.socket(socket.AF_INET, socket.SOCK_RAW,1) #create a raw socket
ip = ("127.0.0.1",3000) # local raw socket adress and port
s.bind(ip)

print("Connecting..")
while True:
    data = s.recv(1024)
    if not data:

        break
    else:
        print(data)
