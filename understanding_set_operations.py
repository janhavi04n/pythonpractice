# -*- coding: utf-8 -*-
"""
Python sets are enclose in {} like a dictionary
but in case of set there is no key-value pair

Sets are unordered with containing only unique values
Similar to math sets and have the same kind of operations
like union, intersection, difference

values added to a set must be hashable - just like a dictionary key
adding any object like list to a set will return a unhashable error
"""
indoor_sport = {'chess', 'table tennis', 'carrom', 'badminton', 'fencing'}
# this will not print values in same order always as set is unordered 
print(indoor_sport) 
print(type(indoor_sport))
# set is unordered but can iterate over a set
for sport in indoor_sport:
    print(sport)
    
another_sport_set = {'table tennis', 'fencing', 'carrom', 'chess', 'badminton'}
# check if 2 sets are equal
if indoor_sport == another_sport_set:
    print('The two sets are Equal')
else:
    print('The two sets are not equal')
# The above prints The two sets are Equal because both sets contain
# the same data
# this differs from list and tuple because in list or tuple
# for 2 list/tuples to be equal they should contain the same data 
# and in the same order

farm_animals = {'cow', 'goat', 'horse', 'sheep', 'hen'}
# below line will return a TypeError: 'set' object is not subscriptable
# this shows set is unordered. 
# goat = farm_animals[1]
# above line will also mean we cannot index a set
# hence no slice can be created from a set
# farm_animals[1:4] - cannot be called on a set
wild_animals = {'horse', 'sheep', 'tiger', 'lion', 'bear'}

# to create a set 
# if we have to create an empty set, then just giving empty
# curly braces will not create an empty set as python will
# create it as a dictionary
numbers = {}
print(numbers, type(numbers))
# we can create a empty set with a set literal as follows
values = {*""}
print(values, type(values))
# we can add elements to a set with the .add method
values.add(10)
values.add(12)
values.add(10)
print(values)

# can create set by passing range to the set function
odd = set(range(1,50,2)) 
print(odd)
# clear method of set clears all elements from the set
odd.clear()
print(odd)

# discard method will remove the element from the set
sports = {'football', 'cricket', 'hockey', 'swimming', 'boxing', 'marathon', 'cycling'}
# if the value passed to discard is not present in the set the program will
# continue and not throw any Error
print(sports)
sports.discard('swimming')
# now swimming is not present in the set as we have called discard
print(sports)
sports.discard('javelin')
# javelin is not present in the set but the above will not return any Error
print(sports)

# remove method will remove the element from the set
# if element is not present then KeyError is returned
outdoor_sports = {'cricket', 'football', 'boxing', 'javelin', 'marathon'}
print(outdoor_sports)
# calling remove will remove boxing
outdoor_sports.remove('boxing')
print(outdoor_sports)
# calling remove and passing any value which is not present
# below line will return a KeyError
# outdoor_sports.remove('hockey')
# we can include the call to remove in a try-except
