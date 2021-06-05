# -*- coding: utf-8 -*-
"""
hacker rank split and join
"""


def split_and_join(line):
    if line is not None:
        new_line = line.split(" ")
        if len(new_line) == 1:
            return new_line
        return "-".join(new_line)

if __name__ == "__main__":
    line = input("enter a line ")
    print(split_and_join(line))



