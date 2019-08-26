import socket
import sys
import os
s = socket.socket(socket.AF_INET, socket.SOCK_RAW,1)
ip = ("127.0.0.1",3000)
s.bind(ip)
#rep = os.system("ping  "+ server_ip)
print("Connecting..")
while True:
    data = s.recv(1024)
    if not data:

        break
    else:
        print(data)
