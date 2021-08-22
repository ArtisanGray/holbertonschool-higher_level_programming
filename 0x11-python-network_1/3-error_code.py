#!/usr/bin/python3
"""this module handles HTTP error codes."""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            print(data.decode('utf-8', 'Strict'))
    except urllib.error.HTTPError as e:
        print("Error code: " + str(e.code))
