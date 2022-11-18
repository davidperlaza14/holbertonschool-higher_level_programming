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

    with Session(engine) as session:
        indx1 = select(State).filter(State.id == 2)
        indx2 = session.execute(indx1).first()
        if indx2 is not None:
            indx2[0].name = "New Mexico"
            session.commit()


if __name__ == '__main__':
    mysqlconnect()
