# -*- coding: utf-8 -*-
"""

hacker rank Lists problem

insert i e: insert i at position e
print: print the list
remove e: remove first ocurrence of e
append e: add e to the end of the list
sort: sort the list
pop: pop last element
reverse: reverse the list

@author: janhavi
"""

numbers = []
n = int(input("enter a number "))

for _ in range(n):
    user_input = input().split(' ')
    command = user_input.pop(0)
    
    if len(user_input) > 0:
        if command == 'insert':
            eval("numbers.{0}({1},{2})".format(command, user_input[0], user_input[1]))
        else:
            eval("numbers.{0}({1})".format(command, user_input[0]))
        
    elif command == 'print':
        print(numbers)
    else:
        eval("numbers.{}()".format(command))
    

