#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return
    nl = set()
    for dat in set_1:
        for dat2 in set_2:
            if dat2 in dat:
                nl.add(dat2)
    return(nl)
