import socket, sys

port = 70
host = sys.argv[1]
print "host: ", host
filename = sys.argv[2]
print "file name: ", filename

s = socket.socket(socket.AF_INET
                  ,socket.SOCK_STREAM
                  )
print "s: ",s

try:
    s.connect((host,port))
except socket.gaierror, e:
    print e
    print "Error conneting to server: %s" % e    
    sys.exit(1)
except:
    print "error!"
    sys.exit(1)


s.sendall(filename + "\r\n")

print "f n: ",(filename + "\r\n")
i = 0
while 1:
    buf = s.recv(2048)
    print "buf: ", buf
    print "len(buf) : ", len(buf)
    if not len(buf):
        break
    sys.stdout.write(buf)
    print "num i is: ", i
    i = i + 1
        
