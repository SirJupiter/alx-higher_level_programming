#!/usr/bin/python3
"""script that changes the name of a State object from the
database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}',
        pool_pre_ping=True
    )

    session = Session(bind=engine)

    try:
        session.query(State).filter(State.id == 2).update(
            {State.name: 'New Mexico'})
        session.commit()
    except Exception as e:
        print(f'Could not change state name: {e}')
