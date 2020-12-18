#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return
    nd = {}
    for item in a_dictionary:
        nd.update({item: a_dictionary[item] * 2})
    return(nd)
