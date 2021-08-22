#!/usr/bin/python3
"""this module requests data from a URL and parses it"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        data = response.read()
        print(response.getheader("X-Request-Id"))
