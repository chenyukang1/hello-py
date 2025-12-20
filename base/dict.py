d = {'Michael': 95, 'Bob': 88, 'Jason': 99}
print(d)
print(d['Michael'])
d['Michael'] = 90
print(d['Michael'])
print('Thomas' in d)
print(d.get('Thomas', -1))

for k, v in d.items():
    print(k, '=', v)
