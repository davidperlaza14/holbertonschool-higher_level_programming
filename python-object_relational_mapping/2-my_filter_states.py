#!/usr/bin/python3
"""Conect the database"""
import sys
import MySQLdb


def mysqlconnect():
    db_connection = None
    db_connection = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306
    )

    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name\
         LIKE BINARY 'N%' ORDER BY states.id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db_connection.close()


if __name__ == '__main__':
    mysqlconnect()
