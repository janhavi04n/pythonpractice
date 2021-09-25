# -*- coding: utf-8 -*-
"""
understanding superset and subset
"""
# subset is a set that has all elements from another set
# proper subset is a set that has elements from another set but
# is not equal to the set

animals = {'dog', 'cat', 'crocodile', 'robin', 'goldfish', 'shark', 'spider',
           'pigeon', 'turtle', 'lizard', 'dragonfly'}
mammals = {'dog', 'cat'}
reptiles = {'crocodile', 'turtle', 'lizard'}
fishs = {'goldfish', 'shark'}
insects = {'spider', 'dragonfly'}
birds = {'robin', 'pigeon'}
zoo_animals = {'crocodile', 'tiger', 'elephant', 'turtle', 'gorilla'}

# subset is written as <=
# proper subset is written as <
# animals is a superset of mammal, reptiles, fish, insects
# the 2 terms are complementary
# e.g. if B is a subset of A, then A is a superset of B
# super set is written as >=
# a proper superset is a set that has elements of another set 
# but it is not equal to it
# proper superset is written as >
# a proper subset contains fewer elements than its superset
# proper superset contains more elements than its subset
# we can check if a set is a subset of another by .issubset() method
# we can check if a set is a superset by .issuperset() method
print(f"reptiles is a subset of animals : {reptiles.issubset(animals)}")
print(f"Zoo animals is a subset of animals : {zoo_animals.issubset(animals)}")
print(f"Animals is superset of birds : {animals.issuperset(birds)}")
print(f"Reptiles is a subset of animals : {reptiles<=animals}")
print(f"Animals is superset of insects : {animals>=insects}")
print(f"Mammals is proper subset of animals : {mammals<animals}")

# disjoint set are sets which have nothing in common with each other
print(f"animal and mammals is disjoint : {animals.isdisjoint(mammals)}")
print(f"fishs and insects is disjoint : {fishs.isdisjoint(insects)}")
