#!/usr/bin/python3
"""this module uses a POST method to send data to a specified URL."""
import requests
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    headers = {'email': email}

    r = requests.post(url, headers)
    print(r.text)
