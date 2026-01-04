# coroutine本质上就是一个增强版的生成器

class Rock:
    def __await__(self):
        value_sent_in = yield 7
        print(f"Rock.__await__ resuming with value: {value_sent_in}.")
        return value_sent_in


async def main():
    print('Beginning coroutine main()')
    rock = Rock()
    print("Awaiting rock...")
    # await calls the __await__() method of the given object.
    # await also does one more very special thing:
    #  it propagates (or “passes along”) any yields it receives up the call chain
    value_from_rock = await rock
    print(f'Coroutine received value: {value_from_rock} from rock.')
    return 32


coroutine = main()
# coroutine.send(arg) is the method used to start or resume a coroutine.
intermediate_res = coroutine.send(None)
print(f'Coroutine paused and returned intermediate value: {intermediate_res}')

print('Resuming coroutine and sending in value: 42.')
try:
    coroutine.send(42)
except StopIteration as e:
    returned_value = e.value
print(f'Coroutine main)_ finished and provided value: {returned_value}')
