#!/usr/bin/env python3

x = ( 1, 'two', 3.0, [4, 'four'], 5)
y = ( 1, 'two', 3.0, [4, 'four'], 5)

print ('x is {}'.format(x))
print (id(x))
print (id(y))
# will show that both are same IDs no need to create a separate object
print (id(x[0]))
print (id(y[0]))


y = [ 1, 'two', 3.0, [4, 'four'], 5]
if isinstance(y, tuple):
   print("yep")
elif isinstance(y, list):
   print("list")
else:
   print("nope")

print(type(x))
print(type(y))
print(id(x))
print(id(y))
