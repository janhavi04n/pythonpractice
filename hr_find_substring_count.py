# -*- coding: utf-8 -*-
"""
hacker rank - count number of times substring appears in a string
input 
string = "ThIsisCoNfUsInG"
substring = is
output = 1

input
string = ABCDCDC
substring = CDC
output = 2

"""


input_string = input()
find = input()

count = 0

while len(input_string) > 0:
    
    if input_string.count(find) > 0:
        count += 1
        pos = input_string.index(find)+1
        input_string = input_string[pos:]
        
    else:
        break
    

print("{0} is present {1} times".format(find, count) )


