# Author : Evren Korkmaz
# This python project create a socket on localhost port 3000
# and take a package from client side.
import socket
import sys
import os

# Create a socket object.
s = socket.socket(socket.AF_INET, socket.SOCK_RAW,1) 
# define a socket port
ip = ("127.0.0.1",3000)
# bind and wait package
s.bind(ip)

print("Connecting..")
while True:
    data = s.recv(1024)
    if not data:

        break
    else:
        print(data)
