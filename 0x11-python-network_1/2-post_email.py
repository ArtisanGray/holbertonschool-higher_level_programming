#!/usr/bin/python3
"""sends a POST"""


if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    data = parse.urlencode({"email": argv[2]}).encode()
    with request.urlopen(argv[1], data=data) as response:
        print(response.read().decode('utf-8'))
        response.close()
