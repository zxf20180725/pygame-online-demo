import socket  # 导入 socket 模块
import time
from threading import Thread

ADDRESS = ('0.0.0.0', 8712)  # 绑定地址
g_socket_server = None  # 负责监听的socket
g_conn_pool = []  # 连接池


def init():
    """
    初始化服务端
    """
    global g_socket_server
    g_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    g_socket_server.bind(ADDRESS)
    g_socket_server.listen(5)
    print_log("服务端已启动，等待客户端连接...")


def accept_client():
    """
    接收新连接
    """
    while True:
        client, _ = g_socket_server.accept()  # 阻塞，等待客户端连接
        # 加入连接池
        g_conn_pool.append(client)
        # 给每个客户端创建一个独立的线程进行管理
        thread = Thread(target=message_handle, args=(client,))
        # 设置成守护线程
        thread.setDaemon(True)
        thread.start()


def message_handle(client):
    """
    消息处理
    """
    client.sendall(("欢迎加入球球聊天室!当前在线人数：%d人" % len(g_conn_pool)).encode(encoding='utf8'))
    while True:
        try:
            bytes = client.recv(1024)  # 接收客户端消息
        except:
            client.close()
            g_conn_pool.remove(client)
            break
        print_log(bytes.decode(encoding='utf8'))  # 打印客户端发送过来的消息

        # 转发给所有在线用户
        for c in g_conn_pool:
            try:
                c.sendall(bytes)
            except:
                c.close()
                g_conn_pool.remove(c)
                break

        if len(bytes) == 0:
            client.close()
            g_conn_pool.remove(client)
            print_log("有一个客户端下线啦！")
            break


def print_log(msg):
    msg = "[" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "] " + msg
    print(msg)


if __name__ == '__main__':
    init()
    # # 新开一个线程，用于接收新连接
    # thread = Thread(target=accept_client)
    # thread.setDaemon(True)
    # thread.start()
    accept_client()
