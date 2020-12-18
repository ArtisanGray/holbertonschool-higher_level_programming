#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return
    nl = set()
    for dat in set_1:
        if dat not in set_2:
            nl.add(dat)
    for dat2 in set_2:
        if dat2 not in set_1:
            nl.add(dat2)
    return(nl)
