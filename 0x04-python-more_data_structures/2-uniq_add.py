#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    nl = []
    sum_int = 0
    for ints in my_list:
        if ints not in nl:
            nl.append(ints)
    for ints in nl:
        sum_int += ints
    return(sum_int)
