
import multiprocessing
import threading
import time


def loop():
    print(f"Thread [{threading.current_thread().name}] start")
    for n in range(0, 6):
        print(f"Thread [{threading.current_thread().name}] at {n}")
        time.sleep(1)
    print(f"Thread [{threading.current_thread().name}] end")


def test_loop_thread():
    print(f"Thread [{threading.current_thread().name}] start")
    t = threading.Thread(target=loop, name='loopThread')
    t.start()
    t.join()
    print(f"Thread [{threading.current_thread().name}] end")

balance = 0
def change_it(n):
    global balance
    balance = balance + int(n) # int(n) 是个函数调用； 这会让 Python 解释器暂停更久，让线程更容易被切换
    balance = balance - int(n)


def test_multi_change():
    def run_thread(n):
        for i in range(1, 10000000):
            change_it(n)
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"balance: {balance}")


def test_multi_change_with_lock():
    lock = threading.Lock()
    def run_thread(n):
        for i in range(1, 10000000):
            lock.acquire()
            try:
                change_it(n)
            finally:
                lock.release()
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"balance: {balance}")

# 解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
# 任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，
# 解释器就自动释放GIL锁，让别的线程有机会执行。
# 这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，
# 即使100个线程跑在100核CPU上，也只能用到1个核
def test_how_many_cores_used():
    def infinite_loop():
        x = 0
        while True:
            x += 1
    cpu_count = multiprocessing.cpu_count()
    print(f"cpu count: {cpu_count}")
    for n in range(cpu_count):
        t = threading.Thread(target=infinite_loop)
        t.start()


def main():
    # test_multi_change()
    # test_multi_change_with_lock()
    test_how_many_cores_used()


if __name__ == "__main__":
    main()
