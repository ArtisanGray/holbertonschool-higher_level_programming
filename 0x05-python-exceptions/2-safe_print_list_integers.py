#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    errc = 0
    while True:
        try:
            if (i < x):
                print("{:d}".format(my_list[i]), end="")
            else:
                break
            i += 1
        except (TypeError, ValueError):
            i += 1
            errc += 1
    print()
    return (i - errc)
