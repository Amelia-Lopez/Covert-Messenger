#!/usr/bin/env python
import socket


HOST = socket.gethostbyname(socket.gethostname())
HOST = "192.168.11.6"  # this is for Mario's computer
DEST_HOST = "192.168.11.1" #this is for Mario's computer
SOURCE_PORT = 555
DEST_PORT = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, SOURCE_PORT))

#src_addr = "\x01\x02\x03\x04\x05\x06"
#dst_addr = "\x01\x02\x03\x04\x05\x06"
payload = ("["*30)+"PAYLOAD"+("]"*30)
#checksum = "\x1a\x2b\x3c\x4d"
#ethertype = "\x08\x01"

print "HOST: " + HOST

s.sendto(payload, (DEST_HOST, DEST_PORT))
