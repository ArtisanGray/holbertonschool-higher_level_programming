#!/usr/bin/python3
for x in range(26):
    if chr(x + 97) is not 'q' and chr(x + 97) is not 'e':
        print("{:s}".format(chr(x + 97)), end="")
