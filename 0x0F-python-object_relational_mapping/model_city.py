#!/usr/bin/python3
""" contains the class definition of a City"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Inherits from Base class

    Attributes:
    __tablename__ (string): table name
    id (integer): unique identifier for each
    name (string): represents a column of a string
    state_id (string): column of integer
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
