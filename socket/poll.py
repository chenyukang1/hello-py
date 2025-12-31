
import select
import socket


def test_poll():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    server.setblocking(False)

    poll_fd = select.poll()
    poll_fd.register(server, select.POLLIN)
    dict = {server.fileno(): server}

    try:
        print('Server start...')
        while True:
            # 线性遍历socket，查看是否有事件
            events = poll_fd.poll(1000)
            for fd, flag in events:
                sock = dict[fd]

                if sock is server:
                    conn, addr = sock.accept()
                    print(f'Connect from {addr}')
                    conn.setblocking(False)
                    poll_fd.register(conn, select.POLLIN)
                    dict[conn.fileno()] = conn

                elif flag & select.POLLIN:
                    data = sock.recv(1024)
                    if data:
                        print(f'Received {data}')
                        sock.send(b'Hello, ' + data)
                    else:
                        print(f'Client {fd} left...')
                        poll_fd.unregister(sock)
                        sock.close()
                        del dict[fd]

    except Exception as e:
        print(f"Error: {e}")
        raise e

    finally:
        server.close()


def main():
    test_poll()

if __name__ == "__main__":
    main()
