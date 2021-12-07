#!/usr/bin/env python3

import os, sys

cwd = os.getcwd()
   
# some non existing directory
fd = 'false_dir/temp'
   
# trying to insert to false directory
try:
    print("Inserting inside-", os.getcwd())
    os.chdir(fd)
except:
    print("Something wrong with specified directory. Exception- ")
    print(sys.exc_info())
             
# handling with finally...this will always run
finally:
    print()
    print("Restoring the path")
    os.chdir(cwd)
    print("Current directory is-", os.getcwd())
