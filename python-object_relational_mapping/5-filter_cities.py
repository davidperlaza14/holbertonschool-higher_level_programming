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
    cursor.execute("SELECT cities.name FROM cities\
    JOIN states ON cities.state_id = states.id\
    WHERE states.name = %(state)s ORDER BY cities.id", {"state": sys.argv[4]})
    cities = cursor.fetchall()

    print(", ".join(city[0] for city in cities))

    cursor.close()
    db_connection.close()


if __name__ == '__main__':
    mysqlconnect()
