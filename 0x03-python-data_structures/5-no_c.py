#!/usr/bin/python3
def no_c(my_string):
    y = len(my_string)
    new_string = ""
    for i in range(y):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            new_string = new_string + my_string[i]
        else:
            i += 1
    return(new_string)
