#!/usr/bin/python3
""" this module opens a http request from URL and parses it."""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    hbtn_read = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(hbtn_read)))
    print("\t- content: {}".format(hbtn_read))
    print("\t- utf8 content: {}".format(hbtn_read.decode('utf-8')))
    response.close()
