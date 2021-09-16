# -*- coding: utf-8 -*-
"""
understanding
shallow copy
deep copy 
wrt dictionaries
"""
import copy

ipl_teams = {
    "Mumbai": "Indians",
    "Chennai": "Super Kings",
    "Bangalore": "Royal Challengers",
    "Delhi": "Daredevils",
    "Kolkata": "Knight Riders",
    "Hyderabad": "Sunrisers",
    "Punjab": "KingsXI",
    "Rajasthan": "Royals"
}


teams_players = {
    "Mumbai" : ['Rohit', 'Bumrah', 'SKY'],
    "Chennai" : ['Dhoni', 'Raina'],
    "Delhi" : ['Dhawan', 'Shaw', 'ShreyasIyer'],
    
}

# this creates a copy of the teams_players dictionary
# which is top_performers
# python goes through each of the dictionary keys
# and copies the key with its value/s into the new dictionary
# the key is a list.
# the first dictionary refers to the list in memory
# second dictionary key also refers to the same list
# which is stored in memory
# so mutating the list will be seen in all the copies
# this is example of shallow copy because the list is not copied
# when the dictionary team_players.copy() is called
# .copy() of dictionary performs a shallow copy
# if the values are immutable values then the reference does not matter

#top_performers = teams_players.copy()

# this creates a deep copy of the teams_players dictionary
# in case of deepcopy the value is also copied to the new
# dictionary instead of the references
# so dict1 and its copy dict2 now have their own copy of the list
# so any change made to the list will be applicable to that 
# dictionary only
top_performers = copy.deepcopy(teams_players)

print(teams_players["Chennai"])
print(top_performers["Chennai"])

top_performers["Chennai"].append("Shardul")
print(teams_players["Chennai"])
print(top_performers["Chennai"])

