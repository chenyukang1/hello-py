import socket
import threading


def test_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('www.sina.com', 80))
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    buffer = []
    while True:
        bytes = s.recv(1024)
        if bytes:
            buffer.append(bytes)
        else:
            break
    s.close()
    data = b''.join(buffer)
    header, html = data.split(b'\r\n', 1)
    print(header.decode('utf-8'))
    with open('sina.html', 'wb') as f:
        f.write(html)


def test_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print('Server start...')

    def tcp_link(sock: socket.socket, addr):
        print(f'Accept new connection from {addr}')
        sock.send(b'Hello')
        while True:
            data = sock.recv(1024)
            if not data or data.decode('utf-8').strip() == 'bye':
                break
            sock.send(f'Hello {data.decode('utf-8')}'.encode('utf-8'))
        sock.close()
        print(f'Connection from {addr} closed')
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcp_link, args=(sock, addr))
        t.start()


def main():
    # test_client()
    test_server()


if __name__ == "__main__":
    main()
