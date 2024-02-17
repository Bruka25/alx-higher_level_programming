#!/usr/bin/python3
"""Python class State, that inherits from
   state
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """ Represents a state for a MySQL database

        __tablename__ (str): The name of the MySQL table to store states
        id: The state's id.
        name: The state's name
        cities: represent the relationship with class City
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
