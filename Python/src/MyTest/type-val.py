#!/usr/bin/env python3

from decimal import *

x = 7
x1 = 7.2
x2 = 7,200
x3 = 'test1'
x4 = "test2"
x5 = -12
a = 8
b = 9
y = ( .1 + .1 + .1) - .3

print('x is {}'.format(x))
print(type(x))
print('x1 is {}'.format(x1))
print(type(x1))
print('x2 is {}'.format(x2))
print(type(x2))
print('x3 is {}'.format(x3))
print(type(x3))
print('x4 is {}'.format(x4))
print(type(x4))
print('x5 is {}'.format(x5))
print(type(x5))
print("-------------------------------")
x = f'seven {a:<09} {b:>09}'
print('x is {}'.format(x))
print(type(x))
print(y)
a = Decimal('.1')
b = Decimal('.1')
c = Decimal('.1')
d = Decimal('.3')
x = a + b + c - d
print(x)

#-------------------------------
#  RESULTS
#-------------------------------
# x is 7
# <class 'int'>
# x1 is 7.2
# <class 'float'>
# x2 is (7, 200)
# <class 'tuple'>
# x3 is test1
# <class 'str'>
# x4 is test2
# <class 'str'>
# x5 is -12
# <class 'int'>
# -------------------------------
# x is seven 800000000 000000009

