import threading


local = threading.local()


def test_thread_local():
    def process_thread(name):
        local.student = name
        print(f"student {local.student} in {threading.current_thread().name}")

    p1 = threading.Thread(target=process_thread, args=("Alice",))
    p2 = threading.Thread(target=process_thread, args=("Bob",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


def main():
    test_thread_local()


if __name__ == "__main__":
    main()
