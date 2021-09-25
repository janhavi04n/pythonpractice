# -*- coding: utf-8 -*-
"""
understanding of set operations like
union
intersect
difference
symmetric difference
"""
# UNION
# union combines 2 or more sets and returns a new set with the elements of
# all the sets
# union is commutative
# which means any way they are combined we get the same output
# like in addition a+b and b+a give the same output
# union of 2 or more sets is defined by .union() method
# or by | operator
# one advantage the method has over operator is that
# we can pass an iterable to the method but in case of operator
# the it has to be both sets
single_sport = {'tennis', 'boxing', 'fencing', 'swimming'}
team_sport = {'tennis', 'cricket', 'football', 'hockey'}

all_sport_1 = single_sport.union(team_sport)
print(all_sport_1)
all_sport_2 = team_sport.union(single_sport)
print(all_sport_2)
all_sport_3 = single_sport | team_sport
print(all_sport_3)

print("-"*80)

# INTERSECTION
# Intersection returns a set which has the common elements from
# two or more sets
# inersection can be created with .intersection() method
# or by & operator
common_sport_1 = single_sport.intersection(team_sport)
print(common_sport_1)
common_sport_2 = team_sport.intersection(single_sport)
print(common_sport_2)
common_sport_3 = single_sport & team_sport
print(common_sport_3)

print("-"*80)

# DIFFERENCE
# difference returns a set which has the difference between 2 or more sets
# difference can be created by the .difference() method
# or the - operator.
# e.g. we have 2 sets s1 and s2
# s1 - s2 : this will return the elements in s1 but not in s2
# s2 - s1 : this will return the elements in s2 but not in s1
# When more than 2 sets are used in difference then 
# the elements are computed from left to right
# so . s1 - s2 - s3 // s1.difference(s2, s3)
# will first compute the difference s1-s2 
# then the diff will be used to compute with s3
man_utd = {'ronaldo', 'rooney', 'van nistelroy', 'giggs'}
real_madrid = {'ronaldo', 'zidane', 'raul', 'ramos'}
juventus = {'ronaldo', 'buffon', 'del piero', 'nedved'}
print(man_utd - real_madrid)
print(real_madrid - man_utd)

print("-"*80)

# SYMMETRIC DIFFERENCE
# symmetric difference of sets s1 and s2 returns a set with elements
# that are in s1 or s2 but not in both
# this is opposite of INTERSECTION
# symmetric difference is created by .symmetric_difference() method
# or by the ^ operator
# In case of multiple sets the symmetric difference is computed from L to R
# multiple sets can be used only with the ^ operator
# with .symmetric_difference() method passing multiple sets returns a TypeError
print(man_utd.symmetric_difference(juventus))
print(man_utd ^ real_madrid ^ juventus)
# following line will return a TypeError
# print(man_utd.symmetric_difference(real_madrid, juventus))
