#!/usr/bin/python3
"""File contains the class definitions of a State and an instance
Base = declarative_base()"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class inherits from Base

    Attributes:
    id (int): id
    name (string): name
    __tablename__ (string): table name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
