#!/usr/bin/python3
"""this module sends a POST request to the specified URL and parses data."""
import requests
import sys


if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    letter = ""
    if (sys.argv[1]):
        letter = sys.argv[1]
        data = {'q': letter}
    else:
        data = {'q': ''}
    r = requests.post(url, data)
    try:
        values = r.json()
        if values == {} or values is None:
            print("[{}] {}".format(values['id'], values['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
