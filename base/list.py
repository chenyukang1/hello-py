classmates = ['Michael', 'Bob', 'Jason']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

classmates.insert(1, 'Jark')
print(classmates)
print(classmates.pop())
print(classmates)
print(classmates.pop(1))
print(classmates)
classmates[1] = 'Sarah'
print(classmates)

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]

# slice L[0:3]表示，从索引0到3，左闭右开区间
print(L[:2])
print(L[-2:])
print(L[-2:-1])

for i, val in enumerate(classmates):
    print(i, val)

print([x for x in range(1, 11) if x % 2 == 0])
