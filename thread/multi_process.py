from multiprocessing import Process
import os

def fork_example():
    print(f"[Process {os.getpid()}] start fork")
    pid = os.fork()
    if pid == 0:
        print(f"[Process {os.getpid()}] I'm child process, parent process {os.getppid()}")
    else:
        print(f"[Process {os.getpid()}] I'm parent process, just created a child process {pid}")

def multiprocessing_example():
    print(f'[Process {os.getpid()}] start multiprocess')
    p = Process(target=run_proc, args=('test',))
    p.start()
    p.join()
    print(f'[Process {os.getpid()}] end')

# 定义子进程执行的方法
def run_proc(name):
    print(f'[Process {os.getpid()}] run {name}')

def main():
    fork_example()
    multiprocessing_example()

if __name__ == "__main__":
    main()
