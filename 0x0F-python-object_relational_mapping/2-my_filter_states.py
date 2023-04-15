#!/usr/bin/python3
"""
Lists  all values in the states table of the database hbtn_0e_0_usa
whose name matches with supplied argument.
Usage: select using <mysql username> |<mysql password> |<database name>| <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    a = db.cursor()
    a.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(sys.argv[4]))
    states = a.fetchall()
    for state in states:
            print(state)
    a.close()
    db.close()
