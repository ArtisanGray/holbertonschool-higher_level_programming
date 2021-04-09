#!/usr/bin/python3
"""send request to URL and displays the body"""


if __name__ == "__main__":
    import requests
    from sys import argv

    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
