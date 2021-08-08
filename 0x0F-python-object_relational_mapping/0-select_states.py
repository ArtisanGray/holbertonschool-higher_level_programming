#!/usr/bin/python3
"""this module is for manipulating MySQL databases."""
import MySQLdb

def main(**kwargs):
    link = MySQLdb.connect(host="localhost", port=3306, **kwargs)
    ms = link.cursor()
    ms.execute("SELECT * FROM states ORDER BY id ASC")
    data = ms.fetchall()
    i = 0
    for item in data:
        print(str(item))
        i += 1
    ms.close()
    link.close()
