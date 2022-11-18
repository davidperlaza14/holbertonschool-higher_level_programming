#!/usr/bin/python3
"""Conect the database"""
import sys
import MySQLdb
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from sqlalchemy import select
from model_state import Base
from model_state import State


def mysqlconnect():
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:\
    {sys.argv[2]}@localhost/{sys.argv[3]}", pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).\
            filter(State.name.contains("a")):
        session.delete(state)
    session.commit()
    session.close()


if __name__ == '__main__':
    mysqlconnect()
