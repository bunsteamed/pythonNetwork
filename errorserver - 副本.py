import socket, traceback, os
host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
print "waiting for connections..."
s.listen(10)

while 1:
	try:
		clientsock, clientaddr = s.accept()
		print "client addr" , clientaddr
		print "client sock" , clientsock
	except KeyboardInterrupt:
		print "KeyboardInterrupt:"
		raise
	except:
		traceback.print_exc()
		print "traceback.print_exc()"	
		continue

	try:
		print "Got connection from", clientsock.getpeername()
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc()
		
	try:
		buf = s.recv(2048)
		if not len(buf):
			break
		sys.stdout.write(buf)
		
		message, address = s.recvfrom(8192)
		print "Got data from", address
		print "Got message: ", message
		s.connect(clientaddr)
		s.sendall(message)
		#s.sendto (message, address)
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc()

	try:
		clientsock.close()
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()
		
		  
