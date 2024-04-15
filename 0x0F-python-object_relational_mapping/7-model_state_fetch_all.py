#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(
    f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}', echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker()
session = Session(bind=engine)

result = session.query(State.id, State.name).all()

for row in result:
    print(f'{row.id}: {row.name}')
# res = [f"{row[0]}: {row[1]}" for row in result]
# print("\n".join(res))
