# -*- coding: utf-8 -*-
"""
understanding the os module
and the paths and directory structure

@author: Janhavi
"""
import os

listing = os.walk('.')

for root, directory, files in listing:
    print(root)
    for d in directory:
        print(d)
    for f in files:
        print(f)
    print('*'*80)
    