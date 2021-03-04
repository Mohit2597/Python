#!/usr/bin/env python3
import os
t_width=os.get_terminal_size().columns
#--> os.get_terminal_size()
#   it will give the width and the height of the terminal coloums
#   os.get_terminal_size().columns
#   it will print the coloums of the terminal window
given_str="MOHIT CHAUDHARY"
print(given_str)

#-- string.center(100)
print(given_str.center(t_width).title())

#--> string.rjust(100)       to print the string in the right side
print(given_str.rjust(t_width).title())

#--> string.ljust(100)
#   justify your string at the starting side of 100 characters
print(given_str.ljust(t_width).title())



#@ lacture 9
