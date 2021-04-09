#!/usr/bin/python3
"""fetches a url"""


if __name__ == "__main__":
    import requests
    from sys import argv

    hdr = requests.head(argv[1])
    print(hdr.headers.get('X-Request-Id'))
