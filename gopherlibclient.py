#from gopherLibClient import gopherlib
#import gopherlib, sys
import sys
import urllib
host = sys.argv[1]
file = sys.argv[2]

f = send_selector(file,host)
for line in f.readlines():
    sys.stdout.write(line)
