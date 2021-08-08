#!/usr/bin/python3
"""this module is for manipulating MySQL databases."""
import MySQLdb
import sys

if __name__ == "__main__":
        link = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
        ms = link.cursor()
        state_name = sys.argv[4]
        ms.execute("SELECT * FROM states WHERE name=%s\
                   ORDER BY id ASC", [state_name])
        data = ms.fetchall()
        for item in data:
            print(str(item))
        ms.close()
        link.close()
