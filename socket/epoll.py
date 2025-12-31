import select
import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9999))
server.listen(5)
server.setblocking(False)
print(f'Server start with fd {server.fileno()}...')

# kqueue（macOS/FreeBSD）比 Linux 的 epoll 还要强大和优雅，因为它不仅仅用于网络:
# 文件监控：它可以监控文件是否被修改、移动或删除（类似 inotify）
# 进程监控：它可以监控某个进程是否退出（NOTE_EXIT）
# 信号处理：它可以把 Unix 信号（比如 SIGINT）转换成一个事件来处理
# 定时器：它可以直接作为一个毫秒级的定时器使用
kqueue = select.kqueue()
kqueue.control([select.kevent(server, select.KQ_FILTER_READ, select.KQ_EV_ADD)], 0)
fds = {server.fileno(): server}

try:
    while True:
        # 内核维护一张事件表，当某socket进来，硬件中断触发回调函数，内核将这个socket扔进就绪队列
        events = kqueue.control(None, 1, 1000)
        for event in events:
            print(f'Event with fd {event.ident} come in')
            sock = fds[event.ident]
            if sock is server:
                if event.filter == select.KQ_FILTER_READ:
                    conn, addr = server.accept()
                    conn.setblocking(False)
                    print(f'Client {addr} connected')
                    fds[conn.fileno()] = conn
                    kqueue.control([select.kevent(conn, select.KQ_FILTER_READ, select.KQ_EV_ADD)], 0)
            else:
                if event.filter == select.KQ_FILTER_READ:
                    data = sock.recv(1024)
                    if data:
                        print(f'Received {data.decode()}')
                        sock.send(b'Hello')
                    else:
                        print(f'Client with fd {sock.fileno()} left...')
                        del fds[sock.fileno()]
                        kqueue.control([select.kevent(sock.fileno(), select.KQ_FILTER_READ, select.KQ_EV_DELETE)], 0)


except Exception as e:
    print(f"Error: {e}")
    raise e
finally:
    server.close()
