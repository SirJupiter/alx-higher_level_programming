#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}',
        pool_pre_ping=True
    )

    session = Session(bind=engine)

    try:
        query = session.query(State.name, City.id, City.name).join(
            City).order_by(City.id).all()
    except Exception as e:
        print(f'Error occurred: {e}')
    else:
        for row in query:
            print(f'{row[0]}: ({row[1]}) {row[2]}')
