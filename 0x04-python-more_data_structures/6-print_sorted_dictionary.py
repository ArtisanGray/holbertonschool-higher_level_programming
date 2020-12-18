#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    n_keys = sorted(a_dictionary.keys())
    for i in range(len(n_keys)):
        print("{:s}: {}".format(n_keys[i], a_dictionary.get(n_keys[i])))
