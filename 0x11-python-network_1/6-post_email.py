#!/usr/bin/python3
"""fetches url"""


if __name__ == "__main__":
    import requests
    from sys import argv

    fet = requests.post(argv[1], data={"email": argv[2]})
    print(fet.text)
