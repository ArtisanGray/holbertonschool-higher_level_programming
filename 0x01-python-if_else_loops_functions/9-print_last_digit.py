#!/usr/bin/python3
def print_last_digit(number):
    div = number % 10
    if number < 0:
        div = -number % 10
    print("{:d}".format(div), end="")
    return(div)
