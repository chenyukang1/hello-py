
print(list(range(1, 11)))

print(x * x for x in range(1, 11))  # generator object
print([x * x for x in range(1, 11)])  # list
print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in "ABC" for n in "XYZ"]) # 两层循环

print([x if x % 2 == 0 else -x for x in range(1, 11)]) # for后面的if是一个筛选条件，不能带else; for前面的部分是一个表达式
