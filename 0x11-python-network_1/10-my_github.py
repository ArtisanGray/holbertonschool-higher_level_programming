#!/usr/bin/python
"""this module grabs the Github ID of a user's authenicated request."""
import requests
import sys


if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    try:
        r = requests.get('https://api.github.com/user', auth=(usr, pwd))
        values = r.json()
        print(values['id'])
    except Exception:
        print("None")
