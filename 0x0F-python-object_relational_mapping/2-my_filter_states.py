#!/usr/bin/python3
"""this module is for manipulating MySQL databases."""
import MySQLdb
import sys

if __name__ == "__main__":
        link = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
        ms = link.cursor()
        ms.execute("SELECT * FROM states WHERE BINARY name='{}'\
                   ORDER BY id ASC".format(sys.argv[4]))
        data = ms.fetchall()
        for item in data:
            print(str(item))
        ms.close()
        link.close()
