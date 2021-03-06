import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'

port = 8712  # 设置端口

s.bind((host, port))  # 绑定端口

s.listen(5)  # 设置最大等待数

while True:
    c, addr = s.accept()  # 建立客户端连接。（会阻塞线程）
    print('有新的客户端加入了：', addr)
    c.send('你好啊！'.encode('utf8'))
    c.close()
