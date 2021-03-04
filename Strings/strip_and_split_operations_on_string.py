#!/usr/bin/env python3

#-->x.strip()
#   x.rstrip('Ptyhon')
#   x.lstrip('Python')
#   it will remove spaces either left side or right side of the character by default it checks for un-nessasery spaces
#   but you can provide any value it will strip that value off if it is in starting or ending for character it must be in either
#   starting of charcter or ending of character not the middle one

#-->x.split()
#   by default based upon spaces your string will be divided into parts

x=" Python"
print(x.strip())
print(x.strip(' Py'))
#$ Python
#$ thon


y="pyhon Scripting is easy python"
print(y.rstrip('python'))
#$ pyhon Scripting is easy |                                ***Note space is also there only the python is removed

###################################
x="python is easy"
print(x.split())
#$ ['python', 'is', 'easy']

print(x.split('is'))
#$ ['python ', ' easy']


#@lacture 7
