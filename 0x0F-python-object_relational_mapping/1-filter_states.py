#!/usr/bin/python3
'''lists all states from htbn 0e that start with capital N'''

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    db_curs = db.cursor()
    db_curs.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id;")
    db_data = db_curs.fetchall()

    for item in db_data:
        print(item)

    db_curs.close()
    db.close()
