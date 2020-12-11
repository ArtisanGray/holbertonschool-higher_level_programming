#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num = 0
    print("{:d} argument".format(len(sys.argv) - 1), end="")
    if len(sys.argv) == 1:
        print("s.")
    elif len(sys.argv) == 2:
        print(":")
    else:
        print("s:")
    for arg in sys.argv:
        num += 1
        if num > 1 and len(sys.argv) > 1:
            print("{:d}: {:s}".format(num - 1, arg))
        elif len(sys.argv) == 1:
            print(".", end="")
