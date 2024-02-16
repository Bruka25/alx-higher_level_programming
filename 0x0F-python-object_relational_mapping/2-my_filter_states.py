#!/usr/bin/python3

""" Python script that displays the state
    that has been queried from the database
    using the given argument
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
    arg = """SELECT id, name
         FROM states
         WHERE name='{}'
         ORDER BY id ASC""".format(sys.argv[4])
    cur.execute(arg)
    arg_states = cur.fetchall()

    for state in arg_states:
        if (state[1] == sys.argv[4]):
            print(state)

    cur.close()
    db.close()
