# -*- coding: utf-8 -*-
"""
hacker rank - mutate string

Task
Read a given string, change the character at a given index 
and then print the modified string.

e.g.
input1 = hellpworld - given string
input2 = 4 - index
input3 = o - change the character at input2 location with input3

output=helloworld
"""

def mutate_string(string, position, character):
    if position >= len(string):
        print('enter position value between 0 and {}'.format(len(string)-1))
        return string
    chars = list(string)
    chars[position] = character
    return "".join(chars)
    


if __name__ == "__main__":
    input_string = input('enter string ')
    pos = int(input('enter position to change '))
    char = input('input char to add ')
    
    print('original string {}'.format(input_string))
    new_string = mutate_string(input_string, pos, char)
    print('after change {}'.format(new_string))

