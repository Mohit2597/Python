#!/usr/bin/env python3

#-->getpass()
#   prompts the user for a password without echoing. The getpass module provides a secure way to handle
#   the password pormpts where programme interact with the users via a terminal.

#-->getuser()
#   function display the login name of the user. the function checks the enviourment variable
#   LOGNAME, LNAME, and USERNAME, in order and return the value of first non-empty strings.

import getpass
dbpass=getpass.getpass(prompt='Password Bro: ')
print(db_pass())
print(f'The password is : {dbpass}')


getpass.getuser()
#$ Mohit
