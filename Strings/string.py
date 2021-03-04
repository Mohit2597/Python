#!/usr/bin/env python3

#what is string in Python?
#--> a string the sequence of characters
#-->computer's don't deal with characters, they work with binary at the end of the day everything will be manupilated and
#   stored in 0's and 1's
#-->the conversion of string into binary is called coading and the reverse process is the decoding. ASCII and unicode
#   populer coading techniques
#-->in Python string is a sequence of unicode characters. Unicode was introduced to include all characters in every language
#   and bring uniformatiy the coading

#-->you can't modify your part of strings
#   python="Hello World"
#   python[4]="n"
#   #$ error you cannot modify it

#--> you cannot delete part of your string
#   del python[4]
#   #$ error can't delete part of string

#--> you cannot modify or delete part of your string but you can completely modify your string
#--> if your string len is 10 than it means it has index values {0-9} and -ve way {-16 to -1}

#--> concatination can be done like this
#   string3=string1+string2
#   string3=string1+" "+string2

name='Narendra'
new_name='Python Devloper'
my_info="""I started my carrer as admin and moved into automation"""

print(f'my name is : {name} \nmy new name is : {new_name} \nmy info is : {my_info}')
# whatever you will type in b/w """(tripel quotation the same format will be preserved even when you will be printing it)

##########################################################
my_string=""
my_string_new=" "
print(f'{bool(my_string_new)}')

#True
#in Python space is also considerd as a character
##########################################################

# HOW TO ACCESS CHARACTERS IN THE STRING
my_fav_scripting="python scripting"

#--> based upon index value you can access items in the strings
#--> python assigns +ve index values and also assigns -ve index values last character index always start with -1
print(my_fav_scripting[5])
#$ n

print(my_fav_scripting[10])
#$ i

print(my_fav_scripting[-1])
#$ g

#--> starting from 0 and goes to 10 means it will print 9 characters from the strings
print(my_fav_scripting[0:10])
#$ python scr


print(my_fav_scripting[0:])
#$ python Scripting

#--> you can also store your string value in other variable and use it
scripting_var=my_fav_scripting[0:6]
print(scripting_var)
#$ python



#################################################################
#FINDING LENGHT OF STRING
#--> len

home="find the length of this string"
print(len(home))
print(f'The length of given string is {len(home)}')
#$ 30
#$ The length of given string is 30


#################################################################
#HOW TO CONCATINATE TWO STRINGS

string1="Mohit"
string2="Chaudhary"
space_string=" "
string_without_space=string1+string2
string3=string1+space_string+string2
print(string_without_space)
print(string3)

#$ Mohit Chaudhary
#$ MohitChaudhary

#preferred always
string4=string1+" "+string2
print(string4)
#$ Mohit Chaudhary

#@lacture3
