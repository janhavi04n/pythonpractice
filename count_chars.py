# -*- coding: utf-8 -*-
"""
returns the number of unique chaacters in a string.
1. ignore case
2. spaces and special chars do not count

"""
text = "To boldly go where no man has gone before today"

chars_dict = {}

chars_in_text = list(text)

for char in chars_in_text:
    if char.isalnum():
        chars_dict[char.casefold()] = chars_dict.setdefault(char.casefold(), 0) +1

print()

for items in sorted(chars_dict.items()):
    print(f"{items}")
