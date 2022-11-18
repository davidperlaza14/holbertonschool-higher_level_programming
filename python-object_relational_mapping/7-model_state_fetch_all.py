#!/usr/bin/python3
"""Conect the database"""
import sys
import MySQLdb
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from model_state import Base
from model_state import State


def mysqlconnect():
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:\
        {sys.argv[2]}@localhost/{sys.argv[3]}")
    with Session(bind=engine) as session:
        x = session.query(State).all()
        for indx in x:
            print(f"{indx.id}: {indx.name}")


if __name__ == '__main__':
    mysqlconnect()
