# -*- coding: utf-8 -*-
"""
how deep copy works - user defined deep copy function
"""
from ipl_players import ipl_teams


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


print(f"IPL teams {ipl_teams}")
new_ipl_teams = my_deep_copy(ipl_teams)
print(f"New IPL teams dict created {new_ipl_teams}")

new_ipl_teams["ChennaiSuperKings"].append("Shardul")
print(f"Updated new ipl teams dict {new_ipl_teams}")
print(f"After update of new dict original remains same {ipl_teams}")
