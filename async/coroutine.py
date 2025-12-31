# Python对协程的支持是通过generator实现的

def consumer():
    r = ''
    while True:
        n = yield r
        if n is None:
            return
        print(f'[Consumer] consuming {n}')
        r = '200 OK'

def produce(c):
    c.send(None)
    for n in range(0, 6):
        print(f'[PRODUCER] producing {n}')
        r = c.send(n)
        print(f'[PRODUCER] consumer return {r}')
    c.close()

c = consumer()
produce(c=c)
