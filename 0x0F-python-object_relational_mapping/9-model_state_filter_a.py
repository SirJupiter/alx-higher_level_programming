#!/usr/bin/python3
"""script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')

    session = Session(bind=engine)

    result = session.query(State).filter(
        State.name.contains('a')).order_by(State.id).all()

    for row in result:
        print(f'{row.id}: {row.name}')
