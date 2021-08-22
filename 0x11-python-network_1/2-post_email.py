#!/usr/bin/python3
"""this module send data to the specified URL (if valid.)"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        grabbed = response.read()
        print(grabbed.decode('utf-8', 'Strict'))
