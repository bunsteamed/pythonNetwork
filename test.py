import socket,sys

host = "localhost" #sys.argv[1]
textport = 51423 #sys.argv[2]


port = int(textport)


#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.connect((host,port))
print "enter data:"
data = sys.stdin.readline().strip()

s.sendall(data)

#s.sendto('',(host,port))


while 1:
	buf = s.recv(2048)
	if not len(buf):
		break
	print "return words: "
	sys.stdout.write(buf)
	
