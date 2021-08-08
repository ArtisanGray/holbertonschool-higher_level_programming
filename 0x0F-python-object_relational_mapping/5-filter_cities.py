#!/usr/bin/python3
"""this module is for manipulating MySQL databases."""
import MySQLdb
import sys

if __name__ == "__main__":
        link = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
        ms = link.cursor()
        state_name = sys.argv[4]
        ms.execute("SELECT cities.name\
                   FROM cities INNER JOIN states\
                   ON cities.state_id = states.id WHERE states.name=%s\
                   ORDER BY cities.id ASC", [state_name])
        data = ms.fetchall()
        i = 0
        for item in data:
            if (len(item) > 0):
                print(str(item[0]), end='')
                if (i < len(data) - 1):
                    print(', ', end='')
                    i += 1
                else:
                    print()
        ms.close()
        link.close()
