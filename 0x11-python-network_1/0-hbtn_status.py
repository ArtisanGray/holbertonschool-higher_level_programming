#!/usr/bin/python3
import urllib.request
"""this module grabs data from a specified URL"""

if __name__ == "__main__":
    response = urllib.request.urlopen("https://intranet.hbtn.io/status")
    data = response.read()
    print(data)
