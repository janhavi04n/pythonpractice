"""
understanding dict
Dictionary is a data structure which stores data as a key-value pair
Key is always a immutable type - so a tuple can be used as a key
Keys dont have to be of same type as long as they are immutable
Keys are always unique. if the same key is added again then the
old value is overwritten by the new one
Keys are always case sensitive - for strings
Value can be anything. It can also be another dictionary
Dictionarys can be nested
"""
# ways to create a dict in python
# with key and values
d1 = {
    "Mumbai": "Indians",
    "Chennai": "Super Kings",
    "Bangalore": "Royal Challengers",
    "Delhi": "Capitals",
    "Kolkata": "Knight Riders",
    "Hyderabad": "Sunrisers",
    "Punjab": "KingsXI",
    "Rajasthan": "Royals"
}

# as a list of tuples passsed to dict function
d2 = dict(
    [
        ("Mumbai", "Indians"),
        ("Chennai", "Super Kings"),
        ("Bangalore", "Royal Challengers"),
        ("Delhi", "Capitals"),
        ("Kolkata", "Knight Riders"),
        ("Hyderabad", "Sunrisers"),
        ("Punjab", "KingsXI"),
        ("Rajasthan", "Royals")
    ]
)

# if keys are strings then they can be passed as keyword args to dict function
d3 = dict(
    Mumbai="Indians",
    Chennai="SuperKings",
    Delhi="Capitals"
)

# to get a value from a dictionary, access it via its key
print(d2["Mumbai"])

# if the key does not exist it throws a KeyError.
# print(d3["Bangalore"])

# can use get() function to get the value from a dictionary
# this is preferred over dictionary["key"] as it will not
# throw KeyError if key does not exist. It will simply
# return None
print(d3.get("Bangalore"))

# above can be handled to return some default instead of None
# if key does not exist
print(d3.get("Bangalore", "Not present"))

# to add to a dictionary we can simply add a key-value as
d3["Delhi"] = "Daredevils"
print(d3)

# updating the values in a dictionary we can update by setting
# a value to a key
# this will update the previously added value if key is present
# else add as above
d3["Delhi"] = "Capitals"
print(d3)

d3["Gujarat"] = "Lions"
print(d3)
# to remove a value from a dictionary
del d3["Gujarat"]
print(d3)

# if removing a key which does not exist
# then it throws a KeyError
# del d3["Bangalore"]

# incremental creation of dictionary
# start with a empty dictionary
d4 = {}
# then keep adding key-values
d4["name"] = "John Doe"
d4["age"] = 25
d4["subjects"] = ["python", "Java", "history", "economics"]
d4["teams"] = {"cricket":"MumbaiIndians", "football":"Barcelona"}
print(d4)

# above dictionary has list and another dictionary as values
# to get values
# this prints the entire list
print(d4["subjects"])
# since value of key subjects is a list. we can access values
# of the returned list individually as
print(d4["subjects"][-1])
# this prints the dictionary
print(d4["teams"])
# values of the inner dictionary can be accessed by its key
print(d4["teams"]["football"])

# tuples can be used as keys since they are immutable
d5 = {
    (0, 0): "00",
    (0, 1): "01",
    (0, 2): "02"
}
print(d5)

# to get pass the tuple
print(d5[(0, 1)])

# to check if any key exists in the dictionary
# this is useful to prevent any KeyErrors
print("Kolkata" in d3)

# to find the number of key-value pairs in the dictionary
print(len(d2))

# items - returns a view object which can be converted as a list
# this list = will be a list of tuples
print(list(d1.items()))

# keys - returns a view object of all the keys
print(list(d1.keys()))

# values - returns a view object of all the values
print(list(d1.values()))

# pop - removes the key from the dictionary and returns the value
print(d2.pop("Bangalore"))

# if key is not present in the dictionary then pop returns KeyError
# to avoid KeyError use the default parameter
print(d2.pop("Pune", "not found"))

# popitem - removes the last added item from the dictionary
# and returns it as a tuple. if the dictionary is empty
# popitem returns a KeyError
print(d3.popitem())

# update - merges the values of dict2 into dict1
# e.g. dict1.update(dict2)
# if any key in dict2 is already present in dict1 then
# value for that key is overwritten else new is added
d_orig = {
    "a": 1,
    "b": 200,
    "c": 3
}
d_new = {
    "d": 4,
    "e": 5,
    "b": 2
}
print(d_orig)
print(d_new)
d_orig.update(d_new)
print(d_orig)

# can also pass a list of tuples or keyword arguments
d_1 = {
    1: "one",
    2: "two"
}
print(d_1)
d_1.update([(3, "three")])
print(d_1)

d_2 = {
    1: "one",
    2: "two"
}
print(d_2)
d_2.update(
    three="three",
    four="four"
)
print(d_2)

# another way of iterating over a dictionary
# items will return a list of tuples and iterating
# will unpack each tuple into key, value
for key, value in d1.items():
    print(key, value, sep=", ")