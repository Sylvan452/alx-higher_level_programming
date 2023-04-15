#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: select using <mysql username> \ <mysql password> \<database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    a = db.cursor()
    a.execute("SELECT * FROM `states`")
    [print(state) for state in a.fetchall()]

