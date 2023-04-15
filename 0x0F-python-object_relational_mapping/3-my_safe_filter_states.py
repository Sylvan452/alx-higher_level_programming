#!/usr/bin/python3
"""
Lists  all values in the states table of the database hbtn_0e_0_usa
whose name matches with supplied argument.
Safe from SQL injections
Usage: select using <mysql username> |<mysql password> |<database name>| <state name searched>
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
