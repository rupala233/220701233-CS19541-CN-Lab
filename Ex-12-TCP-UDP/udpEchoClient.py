import sys
from socket import *

ECHO_PORT = 55555
BUFSIZE = 1024
host = "127.0.0.1"
addr = host, ECHO_PORT

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))

print('udp echo client ready, reading stdin')

while 1:
    line = sys.stdin.readline()
    if not line:
        break
    s.sendto(line.encode(), addr)
    data, fromaddr = s.recvfrom(BUFSIZE)
    print('client received %r from %r' % (data, fromaddr))
