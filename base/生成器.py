# 在Python中，一边循环一边计算的机制，称为生成器

print(x * x for x in range(1, 11)) # generator object

g = (x * x for x in range(1, 11)) # generator也是可迭代对象
for n in g:
    print(n)

# 如果一个函数定义中包含yield关键字，它是一个generator函数
print("-" * 32 + " fab " + "-" * 32)
def fib(max):
    a, b, n = 0, 1, 0
    while n < max:
        yield b
        a, b, n = b, a + b, n + 1

f = fib(6)
print(f)
for n in f:
    print(n)
print("-" * 32 + " fab " + "-" * 32)

# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def odd():
    print('Step 1')
    yield 1
    print('Step 2')
    yield 2
    print('Step 3')
    yield 3

o = odd()
print(next(o))
print(next(o))
print(next(o))
print(next(o))
