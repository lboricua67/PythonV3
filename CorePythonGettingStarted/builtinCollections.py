x = (10, 1, 25, 1, 35, 1 , 25, 10, 25, 11, 0)

print(len(x))

for i in range(len(x)):
    print(x[i])

a = "hola pendejo here I am"

print(len(a))

y=a.count('e')

print(y)

a = "unforgetable"
print(a.partition('get'))

a ="database:IP:port:sid"
y = a.partition(':')
for a in y:
    print(a)

a="the age of {1} is {0}:".format('old', 45)
print(a)
a="the age of {} is {}:".format(45, 'old')
print(a)

#Ranges
print(range(0, 5))           #start stop
print(list(range(5,10)))     #start stop
print(list(range(0,20,2)))   #step by 

t = [ 6, 200, 500, 125, 95 ]
for p in enumerate(t):
    print(p)

for i, v in enumerate(t):
    print(f"i={i}, v={v}")

a = [1, 22, 3, 99, 260, 100, 90, 123456]
print (a[-1])   # print last item in list
print(a[0:-1])  # print first and last items of lsit
print(a[:])     # print list
print(a[:3])    # print first 3 items in list
print(a[3:])    # print everything after 3rd index

c = a
b = a.copy()
print(id(a))   # id of a
print(id(c))   # id of c references a storage
print(id(b))   # id of b references a newer object

d = a[:]       # same as copy
print(id(d))   # will reference new storage
e = list(a)    # will copy entire list
print(id(e))   # will reference new storage
print('--------------------------------------------------')
e.append(35)
print(e)
print(a)
print(b)
print(c)
print(d)
print('--------------------------------------------------')
a.append(666)  # this will impact both list of 'a' and 'c' as they point to same reference
d.append(99999)
print(b)
print(c)
print(d)
print(e)

# ----------------------------------------
# Dictionary processing

a = { 'a': 1, 'b': 3, 'd': 5}

for keys in a:
    print(f'{keys}')

for keys in a:
    print(f'{keys} ==> {a[keys]}')

for val in a.values():
    print(val)

for key, value in a.items():
    print(f'key is: {key} and its value is {value}')

if 'b' in a:
    print('I found it')

from pprint import pprint as pp
pp(a)

# ------------------------------------------
# dealing with sets

b = {9, 6, 7 , 8, 25, 45, 9, 7}  # as this is a set, duplicates are discareded
c = {1, 2, 3, 4, 5, 99, 105}
print(type(b))
print(b)
print(len(b))

#just like math you have union/intersect/diff
print(b.union(c))
print(b.difference(c))
print(b.intersection(c))
print(b.symmetric_difference(c))