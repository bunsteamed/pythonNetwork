import socket, traceback
host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))

i = 0

while 1:
	print "waiting..."
	print "i is %d" % i
	i += 1
	try:
		message, address = s.recvfrom(8192)
		print "Got data from", address
		print "Got Messages: " , message
		s.sendto(message,address)
	except (KeyboardInterrupt, SystemExit):
		print "KeyboardInterrupt:"
		raise
	except:
		traceback.print_exc()
		print "traceback.print_exc()"	
	
	
		
		  
