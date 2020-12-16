#!/usr/bin/python3
def check_len(tuple_x=()):
    if tuple_x is not None:
        if len(tuple_x) == 1 or len(tuple_x) == 0:
            tup = (tuple_x[0], 0)
            return(tup)
        else:
            tup = tuple_x
            return(tup)
    elif tuple_x is None:
        tup = (0, 0)
        return(tup)


def add_tuple(tuple_a=(), tuple_b=()):
    tt1 = check_len(tuple_a)
    tt2 = check_len(tuple_b)
    nt = (tt1[0] + tt2[0], tt1[1] + tt2[1])
    return(nt)
