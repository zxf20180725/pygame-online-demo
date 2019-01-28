import socket

s = socket.socket()
host = '127.0.0.1'
port = 8712

s.connect((host, port))

ret = s.recv(1024)
print(ret.decode('utf8'))

s.send('ni'.encode('utf8'))
s.send('zai'.encode('utf8'))
s.send('gan'.encode('utf8'))
s.send('ma'.encode('utf8'))

s.close()
