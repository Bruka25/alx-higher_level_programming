#!/usr/bin/python3
""" Python script that displays the state
    that has been queried from the database
    using the given argument, but safe
    from sql injection
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
         WHERE name=%s
         ORDER BY id ASC"""
    cur.execute(arg, (sys.argv[4],))
    arg_states = cur.fetchall()

    for state in arg_states:
        print(state)

    cur.close()
    db.close
