#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return
    tmp_d = a_dictionary.copy()
    for key in tmp_d:
        if a_dictionary.get(key) == value:
            a_dictionary.pop(key, None)
    return(a_dictionary)
