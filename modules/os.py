#!/usr/bin/env python3
#
#   os.sep                                      (filed saperator)
#   path='/User/mohit/Desktop/Python'
#   os.getcwd()                                 (current working directory)
#   os.chdir('path')                            (change directory)
#   os.listdir()                                (list files and directories)
#   os.listdir('path')
#   os.mkdir('dir_name')                        make directory
#   os.makedirs('Full_recursive_path')          recursive_directory_make
#   os.remove()
#   os.removedirs('Full_recursive_path')        remove dirs
#   os.rmdir()
#   os.rename(src,dst)                          rename a file or directory
#   os.environ                                  enviourment variables
#   os.getuid()                                 userid
#   os.getgid()                                 groupid
#   os.getpid()                                 get process id
#
#   dir(os.path)
#   os.path.sep                                 path saperator
#   os.path.basename('path')                    basename
#   os.path.join('path1','path2')               join paths
#   os.path.split('path')                       split the path
#   os.path.size('file/folder_path')            find the size of the file
#   os.path.exists('path')                      check path exists or not
#   os.path.isfile('path')                      check file or not (True or false in result)
#   os.path.islink('path')                      check for the soft link         (True/False)
#
#   os.system('mac_command')                    execute operating system command
#
#   print(list(os.walk('path')))                path walk
#
#import os
#for each in list(os.walk('/Users')):
#    print(each)

#for r,d,f in list(os.walk('/Users')):
#for r,d,f in list(os.walk('/Users',topdown=False)):                path down to top
#    print(f)
#    for each_file in f:
#        print(each_file)
