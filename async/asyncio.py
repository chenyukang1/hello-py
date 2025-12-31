import asyncio
import threading


async def hello(name):
    print(f'Hello {name}! ({threading.current_thread()})')
    await asyncio.sleep(1)
    print(f'Hello {name} again! ({threading.current_thread()})')
    return name

async def main():
    L = await asyncio.gather(hello('Bob'), hello('Alice'))
    print(L)

asyncio.run(main=main()) # 所有函数均由同一个线程执行，两个hello()是并发执行的

async def wget(host):
    print(f'wget {host}')
    reader, writer = await asyncio.open_connection(host, 80)
    header = f"GET / HTTP/1.0\r\nHost: {host}\r\n\r\n"
    writer.write(header.encode('utf-8'))
    await writer.drain()

    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print(f'{host} header > {line.decode('utf-8').rstrip()}')
    writer.close()
    await writer.wait_closed()
    print(f'Done {host}')

async def wget_mian():
    await asyncio.gather(wget('www.sina.com'), wget('www.sohu.com'), wget('www.163.com'))

asyncio.run(main=wget_mian())
