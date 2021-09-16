# -*- coding: utf-8 -*-
"""
understanding how deepcopy works
"""
from ipl_players import csk_dict
from copy import deepcopy

def my_deep_copy(d: dict) -> dict:
    """
    

    Parameters
    ----------
    d : dict
        dictionary to be copied.

    Returns
    -------
    dict
        a copy of d where the value 
        is the copy of values of original dictionary.

    """
    new_dict = {}
    
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value
        
    return new_dict


print(f"original dictionary {csk_dict}")

# in csk_dict, the value is a list 
# and this list at index 1 has another list
# see how deepcopy and user defined deepcopy works
copy_1 = my_deep_copy(csk_dict)
copy_2 = deepcopy(csk_dict)
print(f"copy_1 created {copy_1}")
print(f"copy_2 created {copy_2}")

print()

csk_dict["Dhoni"][1].append("2011")
print(f"After updating original is {csk_dict}")
print(f"copy_1  {copy_1}")
print(f"copy_2  {copy_2}")

# here copy_2 is created by using deepcopy() function of copy module
# in deepcopy the objects are recursively copied in the new dict
# example the list index 1 contained another list
# so deepcopy will make a copy of that list when copying
# in the my_deep_copy method we are not copying recursively
# hence the inner list will be a shallow copy - ie the reference
# of original will be present hence we see the value changed in copy_1

