import sys,socket,time

s = socket.fromfd(sys.stdin.fileno(),socket.AF_INET,socket.SOCK_STREAM)
