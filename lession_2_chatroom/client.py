import socket
import time
from threading import Thread

client = socket.socket()
client.connect(('foxyball.cn', 8712))


def recv_handler(client):
    while True:
        data = client.recv(1024)
        print_log(data.decode('utf8'))
        if len(data) == 0:
            data.close()
            break


def print_log(msg):
    msg = "[" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "] " + msg
    print(msg)


if __name__ == '__main__':
    thread = Thread(target=recv_handler, args=(client,))
    thread.setDaemon(True)
    thread.start()
    while True:
        msg = "小胖子:" + input("")
        client.sendall(msg.encode('utf8'))
