# -*- coding: utf-8 -*-
"""
hacker rank capitalize
"""
def solve(s):
    
    words = [word.capitalize() for word in s.split(' ')]
    return " ".join(words)

if __name__ == "__main__":
    s = input()
    
    result = solve(s)
    print(result)


