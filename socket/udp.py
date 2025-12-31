import socket
import threading
import time


def test_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 9999))
    print('Server start...')
    while True:
        data, addr = s.recvfrom(1024)
        print(f'Server received {data} from {addr}')
        s.sendto(b'Hello, %s' % data, addr)

def test_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(b'Monkey', ('127.0.0.1', 9999))
    print(f'Client received {s.recv(1024).decode('utf-8')}')
    s.close()


def main():
    test_server()
    t = threading.Thread(target=test_client)
    time.sleep(1)
    t.start()
    t.join()

if __name__ == "__main__":
    main()
