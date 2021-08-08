#!/usr/bin/python3
"""this module manipulates data within a MYSQL database."""
import sys
import MySQLdb

if __name__ == "__main__":
    link = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    ms = link.cursor()
    ms.execute("SELECT * FROM states ORDER BY id ASC")
    data = ms.fetchall()
    for item in data:
        if ('n' in item[1][0] or 'N' in item[1][0]):
            print(item)
    ms.close()
    link.close()
