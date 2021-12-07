#!/usr/bin/env python3

#--------------------------
# Evaluates to false
x = None
x = False
x = 0
#--------------------------
# Evluates to true
x = 1   # Any number other than 0
x = True
x = None
print('x is {}'.format(x))
print(type(x))

if x:
   print('True')
else:
   print('False')
