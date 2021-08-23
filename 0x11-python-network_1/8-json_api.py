#!/usr/bin/python3
"""this module sends a POST request to the specified URL and parses data."""
import requests
import sys


if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    letter = ""
    if (len(sys.argv) > 1):
        if (len(sys.argv[1]) > 0 and sys.argv[1].isalpha() is True):
            letter = sys.argv[1]
    data = {'q': letter}
    r = requests.post(url, data)
    try:
        values = r.json()
        if len(values) > 0:
            print("[{}] {}".format(values['id'], values['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
