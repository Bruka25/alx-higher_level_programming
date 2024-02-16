#!/usr/bin/python3
"""python script that filters states starting
   with a letter 'N' from the database
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    filter = """SELECT id, name
             FROM states
             WHERE name LIKE 'N%'
             ORDER BY id ASC;"""
    cur.execute(filter)
    states_n = cur.fetchall()

    for state in states_n:
        if (state[1][0] == 'N'):
            print(state)

    cur.close()
    db.close()
