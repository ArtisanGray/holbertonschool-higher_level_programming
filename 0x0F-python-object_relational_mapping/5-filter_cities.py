#!/usr/bin/python3
'''lists all states from htbn 0e that start with capital N'''

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    db_curs = db.cursor()
    db_curs.execute("SELECT cities.name\
 FROM cities\
 LEFT JOIN states\
 ON states.id=cities.state_id\
 WHERE states.name='{}'\
     ORDER BY cities.id".format(sys.argv[4]))
    db_data = db_curs.fetchall()

    newl = []
    for item in db_data:
        newl.append(item[0])
    print(", ".join(newl))
    db_curs.close()
    db.close()
