#!/usr/bin/python3
"""Python script that contains a class definition
   of a city
"""
from model_state import State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ Class city that links to mysql table cities

        __tablename__: the name of the table
        id: primary key that represents the column
            of auto-generated unique integers
        name: represents a column of a string of 128
              characters and can't be null
        state_id: foreign key to states id and can't be
                  null
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
