# Author: Evren Korkmaz
# This python code for the raw socket project client side
# When runing the python file, send a custom icmp package to server sokcet 

import struct
import socket
import time
from random import randint
 # calculate the checksum for icmp header.
def checksum(data):
    s = 0
    n = len(data) % 2
    for i in range(0, len(data)-n, 2):
        s+= (data[i]) + ((data[i+1]) << 8)
    if n:
        s+= (data[i+1])
    while (s >> 16):
        s = (s & 0xFFFF) + (s >> 16)
    s = ~s & 0xFFFF
    return s
# This function define the icmp header values 
# and packaging the values with struck.pack
def icmp():
    # if u want change all value 
    type=8
    code=0
    chksum=0
    id=randint(0,0xFFFF)
    seq=0
    #this line send a header value to chksum function for calculate the chkcum
    real_chksum=checksum(struct.pack("!BBHHH",type,code,chksum,id,seq)) 
    # and add all value in a simple pack
    icmp_pkt=struct.pack("!BBHHH",type,code,socket.htons(real_chksum),id,seq)
    return icmp_pkt
# !BBHHH --> B means 1 byte, H means 2 byte.
# ICMP package have  some value (type,code,chksum...). When add a value of this varibles, want to define size of the value.
# In this ICMP package first (B) byte "type" value, second byte (B) "code" value, next 2 Byte (H) "chksum" ...
# If u want to add new variable, must to change real_chksum=chksum... and icmp_pkt line. 

# create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_RAW,1)
# define a server socket information
ip=('192.168.56.101',3000) 
# and connetctions this socket
s.connect((ip))

while True:
    # sending custom package to server socket every half a second 
    time.sleep(.500) 
    s.send(icmp())
