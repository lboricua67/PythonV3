#!/usr/bin/env python3

def sequence(n = 1):
    for i in n:
        print('i is {}'.format(i))

def dict(n):
    for k, v in n.items():
        print('k: {}, v: {}'.format(k, v))


def main():
    a = ( 1, 2, 3, 4, 5)
    sequence(a)
    a = range(10)
    print('-------------')
    sequence(a)
    a = range(5, 50)
    print('-------------')
    sequence(a)
    a = range(5, 100, 5)
    print('-------------')
    sequence(a)
    a = list(range(5))
    a[2] = 42
    print('-------------')
    print(' List ')
    sequence(a)
    a = list(range(5))
    a[2] = 42
    print('-------------')
    print('Dictionary')
    a = {'one': 1,'two': 2, 'three': 3, 'four': 4}
    sequence(a)
    dict(a)

  

if __name__== '__main__': main()


