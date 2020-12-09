#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i * j != 72 and j > i:
            print("{:d}{:d}".format(i, j), end=", ")
        elif i * j == 72:
            print("{:d}{:d}".format(i, j))
