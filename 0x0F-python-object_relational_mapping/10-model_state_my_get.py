#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}',
        pool_pre_ping=True)

    session = Session(bind=engine)

    search = argv[4]

    result = session.query(State.id).filter(
        State.name == search).all()

    if result:
        for row in result:
            print(row[0])
    else:
        print("Not found")
