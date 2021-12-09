#!/usr/bin/env python3
import time

def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

def prtTime():
    print(time.ctime())

def main():
    banner("Ramon is the man")
    prtTime()

if __name__ == '__main__':
    main()