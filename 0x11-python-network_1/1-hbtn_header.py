#!/usr/bin/python3
"""fetches a using urllib"""

if __name__ == "__main__":
    from urllib import request
    import sys

    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
        response.close()
