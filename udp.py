import socket, sys

#host = "wwww.baidu.com" #sys.argv[1]
#textport = 80 #sys.argv[2]

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

try:
	port = int (textport)
except ValueError:
	port = socket.getservbyname(textport,'udp')

s.connect((host,port))
print "enter data to transmit: "
data = sys.stdin.readline().strip()
s.sendall(data)

print "looking for replies; press ctrl-C to stop"

while 1:
	buf = s.recv(2048)
	if not len(buf):
		break
	sys.stdout.write(buf)
	
	

