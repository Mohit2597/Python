#!/usr/bin/env python3

#--> y="-".join(x)
#   can add anything in the place of "-"

#--> x.centre(20)
#   the characters you will provide it will take all the chracter and then try to put your string in the middle of it

#-->x.zfill(10)
#   suppose x=Python now the python has only 6 character but the length you provided is 10 then what zfill will do it
#   will padd the remaining character as 0 in the starting
#   0000Python
#   to complete the string length

x="Python"
y="_".join(x)
print(y)
#$ P_y_t_h_o_n

print("*".join(x))
#$ P*y*t*h*o*n

print("\n".join(x))
#$ P
#$ y
#$ t
#$ h
#$ o
#$ n

print("\t".join(x))
#$ P	y	t	h	o	n


####################################################
print(x.center(20))
#$        Python

mystring="Python Scripting"
print(x.center(20))
print(mystring.center(20))
#$        Python
#$  Python Scripting


#@ lacture 6
