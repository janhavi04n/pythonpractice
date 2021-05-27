# -*- coding: utf-8 -*-
"""

practise for if else elif

"""

answer = 42

guess = int(input("Enter any number : "))

# if you need to check only 2 conditions - this or that then use if-else
if (guess == answer):
    print('The answer to Life, the Universe and Everything is {}'.format(str(answer)))
else:
    print('Wrong answer! get tickets to Vogon Poetry concert')
    
   
# elif = else if. If multiple conditions are to be checked
age = int(input("enter age : "))

if age >= 60:
    print('vaccine in P1')
elif age >= 45:
    print('vaccine in P2')
elif age >= 18:
    print('vaccine in P3')
else:
    print('not eligible')