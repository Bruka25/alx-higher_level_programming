#!/usr/bin/python3
"""Python script for listing cities in the
   given argument, where the argument is
   a state name
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
    sel = """SELECT cities.name
         FROM states
         INNER JOIN cities ON states.id = cities.state_id
         WHERE states.name=%s
         ORDER BY cities.id ASC"""
    cur.execute(sel, (sys.argv[4],))
    all_cities = cur.fetchall()

    print(", ".join([city[0] for city in all_cities]))

    cur.close()
    db.close()
