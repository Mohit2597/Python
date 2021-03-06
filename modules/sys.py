#!/usr/bin/env python3
#-->sys module
#       the sys module is used to work with python runtime enviourment
#       provides functions and variables used to manipulate different parts of the python
#       runtime enviourment

'''
import sys
print(sys.version)
sys.version_info()
print(sys.modules)
print(sys.path)                                             enviourment variable for python
sys.exit()                                                  do't execute
'''

#-->sys.argv
#   returns a list of command line arguments passed to a python script
#   whatever the value you are passing at command line argument it will treat them as a stirng
#   print(sys.argv[0])
#   if your string consists of quotations then you have to use quotations for the entire string e.g. "Ptyhon Scripting"

import sys
if len(sys.argv) !=3:
    print("Usage: ")
    print(f'{sys.argv[0]} <string> <upper/lower>')
    sys.exit()
user_string=sys.argv[1]
user_action=sys.argv[2]

print(f'string: {user_string}\nAction: {user_action}')

#@ lacture4
