
import asyncio
import datetime
import time


async def other_work():
    print("I like work. Work work.")


async def test_custom_async_sleep():
    work_tasks = [
        asyncio.create_task(other_work()),
        asyncio.create_task(other_work()),
        asyncio.create_task(other_work())
    ]
    print(
        "Beginning asychronous sleep at time: "
        f"{datetime.datetime.now().strftime("%H:%M:%S")}."
    )
    await asyncio.create_task(async_sleep(3))
    print(
        "Dnone asynchronous sleep at time: "
        f"{datetime.datetime.now().strftime("%H:%M:%S")}."
    )
    await asyncio.gather(*work_tasks)


async def async_sleep(seconds: float):
    future = asyncio.Future()
    time_to_wake = time.time() + seconds
    asyncio.create_task(_sleep_watcher(future, time_to_wake))
    await future


async def _sleep_watcher(future: asyncio.Future, time_to_wake):
    while True:
        if time.time() > time_to_wake:
            future.set_result(None)
            break
        else:
            await YieldToEventLoop()


class YieldToEventLoop:
    def __await__(self):
        yield


def main():
    asyncio.run(test_custom_async_sleep())


if __name__ == "__main__":
    main()
