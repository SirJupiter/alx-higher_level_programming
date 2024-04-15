#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

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

    new_record = State(name=u'Louisiana')

    try:
        # Add record to the database
        session.add(new_record)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error occurred while adding state: {e}")
    finally:
        result = session.query(State.id).filter(
            State.name == 'Louisiana').first()
        print(result.id)

        session.close()
