#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        val = ord(str[i])
        if (ord(str[i]) <= 122 and ord(str[i]) >= 97):
            val = ord(str[i] - 32)
        print("{:c}".format(val), end="")
    print("")
