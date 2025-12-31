import select
import socket


def test_select():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 9999))
    server.listen(5)
    server.setblocking(False)

    rlist = [server]
    wlist = [server]
    xlist = [server]

    print("Server start...")
    try:
        while True:
            # select每次都要拷贝全量fd数据进出内核
            # select存在1024文件描述符的限制
            readable, writeable, exceptional = select.select(rlist, wlist, xlist)

            for sock in readable:
                if sock is server:
                    conn, addr = sock.accept()
                    print(f"Client {addr} connected")
                    conn.setblocking(False)
                    rlist.append(conn)
                else:
                    data = sock.recv(1024)
                    if data:
                        print(f"Received {data.decode().strip()}")
                    else:
                        print("Client left...")
                        sock.close()
                        rlist.remove(sock)

    except Exception as e:
        print(f"Error: {e}")
        raise e

    finally:
        server.close()


def main():
    test_select()


if __name__ == "__main__":
    main()
