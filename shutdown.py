import socket, sys,time

host = "localhost" #sys.argv[1]
textport = 51423 #sys.argv[2]
filename = "" #sys.argv[3]

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error, e:
    print "error creating socket: %s " % e
    sys.exit(1)

try:
    port = int(textport)
    print "1port : %d" % port
except ValueError:
    try:
        port = socket.getservbyname(textport,'tcp')
        print "2port tcp : %d" % port
    except socket.error, e:
        print "couldn't find your port: %s " % e
        try:
            port = socket.getservbyname(textport,'udp')
            print "2port udp : %d" % port
        except socket.error, e:
            print "couldn't find your port: %s " % e
            sys.exit(1)
        

try:
    s.connect((host,port))
except socket.gaierror,e:
    print "address-related error connecting to server: %s" %e
    sys.exit(1)
except socket.error, e:
    print "connection error : %s " % e
    sys.exit(1)

print "filename"
print "sleeping..."
time.sleep(10)
print "continuing..."

try:
    s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
    #s.sendall("sss")
except socket.error,e:
    print "error sending data: %s" % e
    sys.exit(1)

try:
    s.shutdown(1)
except socket.error,e:
    print "error sending data (detected by shutdown): %s " % e
    sys.exit(1)
    
while 1:
    try:
        buf = s.recv(2048)
    except socket.error,e:
        print "buf error receiving data: %s" % e
        sys.exit(1)
    if not len(buf):
        break
    print u"begin output"
    sys.stdout.write(buf)



    
                      
