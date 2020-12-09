#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    numdiv = (-number % 10) * -1
else:
    numdiv = number % 10
str = "Last digit of"
if numdiv > 5:
    print("{0} {1:d} is {2:d} and is greater than 5".format(
         str, number, numdiv))
elif numdiv % 10 == 0:
    print("{0} {1:d} is {2:d} and is 0".format(
        str, number, numdiv))
else:
    print("{0} {1:d} is {2:d} and is less than 6 and not 0".format(
        str, number, numdiv))
