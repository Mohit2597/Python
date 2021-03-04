#!/usr/bin/env python3

#-->x.count('is')
#   to find out how many times is apperd on the given string can perform this action on a string and on a character also

#-->x.index('p')
#   by default is will look for left to right

#-->x.find('is',9)
#   find out the index location of the character or a given string
#   if 'is' is not present after 9th character then it will give the output as -1 means 'is' is not present after 9th character
#   find
x="python is easy and easy to use language"
count_x=x.count('easy')
print(count_x)

index_x=x.index('is')
print(index_x)
del count_x
#$ 2            (count of x)
#$ 7            (index of x)


y="python is easy and easy to use"
count_y=y.count('is',1)
print(count_y)
#$ 3

index_y=y.index('e',2)
print(index_y)
#$ 10

find_y=y.find('is')
print(find_y)
#$7

find_y=y.find('is',9)
print(find_y)
#$ -1



#@ lacture 8
