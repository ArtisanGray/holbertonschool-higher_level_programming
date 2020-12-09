#!/usr/bin/python3
for i in range(122, 96, -1):
    val = i
    if (i % 2 is not 0):
        val = i - 32
    print("{:s}".format(chr(val)), end="")
