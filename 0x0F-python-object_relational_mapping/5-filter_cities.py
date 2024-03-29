#!/usr/bin/python3
"""
Lists  all cities from  database hbtn_0e_0_usa order by city id
Usage: select using <mysql username> |<mysql password> |<database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    a = db.cursor()
    a.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in a.fetchall() if ct[4] == sys.argv[4]]))

