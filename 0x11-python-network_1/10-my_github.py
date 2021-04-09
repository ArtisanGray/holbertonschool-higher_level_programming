#!/usr/bin/python3
"""displays your GitHub id"""


if __name__ == "__main__":
    import requests
    from sys import argv

    req = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(req.json().get('id'))
