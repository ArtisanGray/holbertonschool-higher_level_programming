#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        return
    if key not in a_dictionary:
        a_dictionary.update({key: value})
    elif key in a_dictionary:
        a_dictionary[key] = value
    return(a_dictionary)
