#!/usr/bin/env python
import socket

"""Debug information taken from here: http://pymotw.com/2/socket/addressing.html"""
def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names."""
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix)
                 )

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')
print families
print ""
print types
print ""
print protocols
print ""
"""end debug information"""

HOST = socket.gethostbyname(socket.gethostname())
HOST = "127.0.0.1"
s = socket.socket(socket.AF_INET, socket.SOCK_RAW)  # Operation not permitted = not running as root
s.bind((HOST, 0))

src_addr = "\x01\x02\x03\x04\x05\x06"
dst_addr = "\x01\x02\x03\x04\x05\x06"
payload = ("["*30)+"PAYLOAD"+("]"*30)
checksum = "\x1a\x2b\x3c\x4d"
ethertype = "\x08\x01"

print "HOST: " + HOST

s.sendto(dst_addr+src_addr+ethertype+payload+checksum, (HOST, 4000))
