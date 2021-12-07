#!/usr/bin/env python3


def f1(f):
    def f2():
        print('this is before function call')
        f()
        print('this is after function call')
    return f2

@f1      #a decorator assings f3 to itself
def f3():
    print('this is f3')

def main():
    print('--------------------------------')
    f3()

if __name__ == '__main__': main()
