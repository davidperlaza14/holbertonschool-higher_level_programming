#!/usr/bin/python3
"""Conect the database"""
import MySQLdb
import sys


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
    cursor.execute("SELECT cities.id, cities.name, states.name\
    FROM states, cities WHERE cities.state_id = states.id ORDER BY cities.id")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db_connection.close()


if __name__ == '__main__':
    mysqlconnect()
