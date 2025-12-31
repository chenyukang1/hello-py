import selectors
import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))
server.listen(5)
server.setblocking(False)
print('Server start')

selector = selectors.DefaultSelector()
serverKey = selector.register(server, selectors.EVENT_READ)

try:
    while True:
        for key, events in selector.select(1000):
            if key.fileobj == server:
                if events & selectors.EVENT_READ:
                    client, addr = server.accept()
                    client.setblocking(False)
                    print(f'Client {addr} connected')
                    selector.register(client, selectors.EVENT_READ)
            else:
                if events & selectors.EVENT_READ:
                    print(f'{key}')
                    data = key.fileobj.recv(1024)
                    if data:
                        print(f'Received {data.decode()}')
                        key.fileobj.send(b'Hello')
                    else:
                        print(f'Client with fd {key.fd} left...')
                        selector.unregister(key.fileobj)

except Exception as e:
    print(f"Error: {e}")
    raise e

finally:
    server.close()
