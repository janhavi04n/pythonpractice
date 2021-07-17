# -*- coding: utf-8 -*-
"""
checks if a word is palindrome
example:
was it a car, or a cat, I saw?
this is a palindrome
"""

def is_palindrome(word):
    rev = word[::-1]
    return rev.casefold() == word.casefold()


def check_for_palindrome(sentence):
    spaces_removed = ""
    for char in sentence:
        if char.isalnum():
            spaces_removed += char
    
    return is_palindrome(spaces_removed)


word2check = input("input any word to check : ")
if check_for_palindrome(word2check):
    print("'{}' is a palindrome".format(word2check))
else:
    print("'{}' is not a palindrome".format(word2check))

