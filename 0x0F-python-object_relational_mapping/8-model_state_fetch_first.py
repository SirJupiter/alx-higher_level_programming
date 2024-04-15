#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine(
    f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/argv[3]')

Base.metadata.create_all(engine)

Session = sessionmaker()
session = Session()

result = session.query(State).first()


