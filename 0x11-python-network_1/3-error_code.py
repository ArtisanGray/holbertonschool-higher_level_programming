#!/usr/bin/python3
"""Takes a URL"""


if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
            response.close()
    except error.HTTPError as err:
        print("Error Code: {}".format(err.code))
