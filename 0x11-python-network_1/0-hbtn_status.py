#!/usr/bin/python3
"""this module grabs data from a specified URL"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        data = response.read()
        print(data)
