#!/usr/bin/python3
"""script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa"""

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
        session.query(State).filter(State.name.contains('a')).delete()
        # Commit the transaction to save the changes in the database
        session.commit()
    except Exception as e:
        print(f'Could not delete rows: {e}')
    finally:
        session.close()
