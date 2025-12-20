from functools import reduce


def f(x):
    return x * x

r = map(f, [x for x in range(1,11)])
print(r)
print(list(r))


def add(x,y):
    return x+y

print(reduce(add, [x for x in range(1, 11)]))
