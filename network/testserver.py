import socket
import sys

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    port = int(textport)
except ValueError:
    port = socket.getserverbyname(textport, 'udp')
s.connect((host, port))
print "Enter data to transmit:"
data = sys.stdin.readline().strip()
s.sendall(data)
print "Looking for replies; press Ctrl-C Ctrl-Break to stop ."
while 1:
    buf = s.recv(2048)
    if not len(2048):
        break
    sys.stdin.write(buf)