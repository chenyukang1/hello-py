# Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节

print('中文')
print(ord('A'))
print(ord('中'))
print(chr(65))
print(chr(25991))

# bytes类型的数据用带b前缀的单引号或双引号表示

x = b'ABC'
print(type(x))
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

# 计算str包含多少个字符，可以用len()函数，如果换成bytes，len()函数就计算字节数

print(len(b'ABC'))
print(len('中文'.encode('utf-8'))) # 1个中文字符经过UTF-8编码后通常会占用3个字节
