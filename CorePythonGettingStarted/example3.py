# str, bytes, list, and dict and for...loops

a1 = "my string is here"
b2 = "more data"
b = ['a', 'b', 'c', 1, 2, 3, 4]
c = {'one': 1, 'two': 2, 'three': 4, 'five': 5}
d = b'data'
e = [1, 2, 3, range(6), [9, 8, 7], 5, (0,1,2,3), bool(0), bool(1), 'ape', 'cat', 'dog']

print(a1 + b2)
print(b)
print(c)

for i in b:
    print(i)

# prints key
for key, value in c.items():
    print(key, value)

for i in c.keys():
    print(i)

for i in c.values():
    print(i)

# bytes would result value of ascii
for i in d:
    print(i)

# checking for specific types
for i in e:
    print(type(i))
    if type(i) == list:
        for a in i:
            print(a)
    elif type(i) == range:
        for a in i:
            print(a)
    elif type(i) == tuple:
        for a in i:
            print(a)
    elif type(i) == str:
        for a in i:
            print(a)

a=[]
a.append('abcd')
for i in range(5):
    x = str(i) + " val"
    a.append(x)
print(a)
print(len(a))
b={}
for i in range(5):
    x = str(i)
    y = i + 3
    b[x] = y

print(b)
b.update({'test': 99})
print(b)
b.clear()
print('after clear')
print(b)