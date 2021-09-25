# -*- coding: utf-8 -*-
"""
exercise 2: find out which prepositions have been used in the quote
"""
text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

preps_used = set()
text_words = text.split()
print(text_words)

preps_used = prepositions.intersection(text_words)
print(f"{preps_used}")
