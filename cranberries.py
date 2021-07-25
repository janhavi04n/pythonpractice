# -*- coding: utf-8 -*-
"""
understanding pickle
1. write to a file
2. read from file
File save with ext .pickle
"""
import pickle

album_data = (
    "No Need to Argue",
    "The Cranberries",
    "1994",
    (
        (1, "Ode to my Family"),
        (2, "I Can't be with you"),
        (3, "Twenty one"),
        (4, "Zombie"),
        (5, "Empty")
    )
   )

with open("cranberries.pickle", "wb") as cranb_file:
    pickle.dump(album_data, cranb_file)
    
print("write to fiele done")

with open("cranberries.pickle", "rb") as read_cranb:
    cranberries_data = pickle.load(read_cranb)
    
print(cranberries_data)

album, artist, year_release, tracks = cranberries_data
print(album)
print(artist)
print(year_release)

for track in tracks:
    track_num, track_name = track
    print(track_num, track_name)
