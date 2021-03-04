#!/usr/bin/env python3
my_list=[2,3,4,"Python",6,7,5.8]
my_empty_list=[]

#   ****IMPORTTANT****
#   modificatin don't use the print
#   if you want to modify the data assign it to new variable and print that variable
#   dir(list)
#    without __something__ these are the opertions you can perform on the lists
#   lists are mutable (means the data of the lists can be modified)
#   id(my_list)             to print the memory location of the my_list variable



#-->bool(my_list)
#   bool is useful when you want to find out weather the given list is empty or not

#-->print(my_list[3])
#   $ Python
#   to print the character of the my_list

#-->print(my_list[3][1])
#   $ P
#   my_list[3] will give out the output as string and as the output is also an string we can perform
#   all the strings operations

#-->print[:]                    will print out the entire string
#   print[2:4]                  from 2 to 4 it will print out the entire my_list
#   print[1:]                   print 1 to last

#-->mylist[0]=45
#   modifying the index 0 data to 45

#-->index()
#   print(my_list.index("Python"))
#   $ 3
#   to find out the index value of the python in the list

#-->count()
#   print(my_list.count('Python'))
#   how many times count is there in the the list

#-->clear()
#   my_list.clear[]
#   it will clear the list values and will provide the empty list

#-->copy()
#   my_new_list=my_list
#   my_new_list=my_list.copy
#   without the copy module whatever the memory location allocated to the my_list variable same memory
#   location will be pointing towards the my_new_list and if you delete the my_list varible you will not
#   be able to use the variable
#   but in my_list.copy a new memory location will be allocated and will be pointint towards this varible
#   to verfiy you can use the commands below
#               print(id(my_list),id(my_new_list))
#               $ 4464209472 4464209472
#
#               print(id(my_list),id(my_list.copy()))
#               $ 4464209472 4463592320

#-->my_list.append(56)
#   by default it will add 56 at the end of the list
#   my_list.insert(1,56)
#   (at index of 1 you have added a new value 56)

#-->my_list.extend()
#   if you have another string and you want to iclude that data of that string into our list
#   if you will use apped() it will add it as an list (list inside the list) but if you want to use
#   2nd list elements inside our exisitng list use extend() to add new_list data in out list as elements
        #   my_new_list=[4,5]
        #   my_list=[89,1,2,3,4,5]
        #   my_list.apped(my_new_list)
        #   #$ my_list=[89,1,2,3,4,5,[4,5]]

        #   my_new_list=[4,5]
        #   my_list=[1,2,3,4,5,6]
        #   my_list.extend(my_new_list)
        #   #$ my_list=[1,2,3,4,5,6,4,5]

#-->my_list.remove('Python')
#   (it will remove the value from the list based upon value)

#-->my_list.pop()
#   remove operations are done based upon index values
#   by default it will remove the last value from the list
#
#   my_list.pop(3)
#   (it will remove the element on index value 3)


#-->my_list.reverse()
#   (it is like the reverse image of your data)

#-->my_list.sort()
#   my_list.sort(reverse=True)                                  sort and reverse

#@ lacture 1
