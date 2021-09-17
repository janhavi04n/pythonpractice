# -*- coding: utf-8 -*-
"""

setdefault method of dict

value = dict_var.setdefault("key_name", default_value)
Above setdefault method will return the value of "key_name"
if it exists in the dictionary
else will create a key "key_name" and set what is set in default_value
and return the value

Works similar to .get("key_name", default_value) except
in .setdefault the key is added to the dict if it doesnt exist
.get will not add the key in the dict, but will just return the 
default
"""

