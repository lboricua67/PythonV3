#!/usr/bin/env python3


def myProc(n=1):
    print('Value of N is: ', n)
    
def myFunc(n=1):
    print('Value of n is: {n}')
    n += 5
    return(n)

def myFunc2(a=1, b=2, c=3):
    print('Values: ', a, b, c)
    return(a,b,c, c+1)

def myProc2(*args):
    if len(args):
       for s in args:
           print(s)
    else:
       print('Meow.')

def myProc3(**kwargs):
    if len(kwargs):
       for k in kwargs:
           print('Kitten {} says {}'.format(k, kwargs[k]))
    else:
       print('Meow.')

def main():
    print('Starting the process!')
    X=myProc(5)
    print('Value of X: ', X)
    
    X=myFunc(25)
    print('Value of X: ', X)
    
    X, Y, Z, A = myFunc2(5, 6, 7)
    print(X, Y, Z, A)

    myProc2('one', 'two', 'three')
    print('----------------------------')
    x = ('one', 'two', 'three')
    myProc2(*x)

    print('----------------------------')
    myProc3(Buffy = 'meow', Zilla ='grr', Angel = 'rawr')
    print('----------------------------')
    x = dict(Buffy = 'meow', Zilla ='grr', Angel = 'rawr')
    myProc3(**x)
    

if __name__ == '__main__': main()
