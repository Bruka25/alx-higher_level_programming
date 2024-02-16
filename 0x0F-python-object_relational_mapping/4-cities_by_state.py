#!/usr/bin/python3
""" python script that retrieves all the
    cities from the states id and lists
    them after joining
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
    sel = """SELECT cities.id, cities.name, states.name
         FROM states
         INNER JOIN cities ON states.id = cities.state_id
         ORDER BY cities.id ASC"""
    cur.execute(sel)
    all_cities = cur.fetchall()

    for city in all_cities:
        print(city)

    cur.close()
    db.close()
