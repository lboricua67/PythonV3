#!/usr/bin/env python3
#
# Author:  Ramon Santiago
#
def function(n = 1):
    print(n)

def isprime(n):
    if n <= 1:
       return False
    for x in range(2, n):
        if n % x == 0:
           return False
    else:
        return True

def list_primes():
    for n in range(10000):
        if isprime(n):
           print(n, end=' ',flush=True)   # flushes buffer
    print()

n=31
if isprime(n):
   print(f'{n} is prime')
else:
   print(f'{n} not prime')

#list_primes()

function()
