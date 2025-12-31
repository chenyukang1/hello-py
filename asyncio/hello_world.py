import asyncio


def test_asyncio_hello_world():
    async def print_hello_world():
        print('Hello...')
        await asyncio.sleep(1)
        print('...World!')
    asyncio.run(main=print_hello_world())


def test_asyncio_task():
    async def loudmouth_penguin(magic_number: int):
        print(
            "I am a super special talking penguin. Far cooler than that printer. "
            f"By the way, my lucky number is: {magic_number}."
        )
    coroutine_obj = loudmouth_penguin(magic_number=3)
    print(coroutine_obj) # async方法创建一个协程对象 <coroutine object>，代表方法的逻辑或主体

    def get_random_number(): # 协程可以在函数体内的不同点暂停和恢复
        print('Hi')
        yield 1
        print('Hello')
        yield 7
        print('Howdy')
        yield 4
    generator = get_random_number()
    print(generator) # 该方法返回一个生成器对象 <generator object>
    print(next(generator)) # 生成器对象运行，然后暂停
    print(next(generator))
    print(next(generator))

    async def run_task():
        task = asyncio.create_task(coroutine_obj)
        print(task)
        await task

    asyncio.run(main=run_task())


def test_await_task():
    async def dig_the_hole():
        print('digging the hole...')

    async def plant_a_tree():
        dig_task = asyncio.create_task(dig_the_hole())
        # when the awaited task finishes (dig_task),
        # the original task or coroutine (plant_a_tree()) is added back
        # to the event loop’s to-do list to be resumed
        await dig_task
        print('dig the hole finish')
        print('plant a tree')

    asyncio.run(main=plant_a_tree())


def test_await_coroutine():
    async def coro_a():
        print("I am coro_a(). Hi!")

    async def coro_b():
        print('I am coro_b(). I sure hope no one hogs the event loop...')

    async def main():
        task_b = asyncio.create_task(coro_b())
        for i in range(3):
            # awaiting a coroutine does not hand control back to the event loop
            await coro_a()
        await task_b

    asyncio.run(main=main())


def test_await_coroutine_v2():
    async def coro_a():
        print("I am coro_a(). Hi!")

    async def coro_b():
        print('I am coro_b(). I sure hope no one hogs the event loop...')

    async def main():
        # 1. task_b enqueue
        task_b = asyncio.create_task(coro_b())
        for i in range(3):
            # 2. 3 task_a enqueue
            await asyncio.create_task(coro_a())
        await task_b

    asyncio.run(main=main())


def main():
    # test_asyncio_task()
    # test_await_task()
    # test_await_coroutine()
    test_await_coroutine_v2()


if __name__ == "__main__":
    main()
