import socket

s = socket.socket()
host = '127.0.0.1'
port = 8712

s.connect((host, port))

ret = s.recv(1024)
print(type(ret),ret.decode('utf8'))

s.close()
