#!/usr/bin/python3
import MySQLdb
"""this module uses the mysql import to manipulate sql databases."""

if __name__ == "__main__":
    link = MySQLdb.connect(host="localhost", port=3306, user="root",
                           passwd="root", db="hbtn_0e_0_usa", charset="utf8")
    ms = link.cursor()
    ms.execute("SELECT * FROM states ORDER BY id ASC")
    data = ms.fetchall()
    i = 0
    for item in data:
        print(str(item))
        i += 1
    ms.close()
    link.close()
