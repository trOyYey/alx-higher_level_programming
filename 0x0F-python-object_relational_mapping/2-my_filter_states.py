#!/usr/bin/python3
""" Getting states that matches userinput argv4"""
import MySQLdb
from sys import argv
host = "localhost"


def main():
    db = MySQLdb.connect(host=host, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states where name LIKE BINARY '{}'\
                 ORDER BY states.id;".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
