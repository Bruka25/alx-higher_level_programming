#!/usr/bin/python3
"""python script that prints all city
   objects from the database
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for cit in session.query(State, City).filter(State.id == City.state_id):
        print("{}: ({:d}) {}".format(cit.State.name, cit.City.id,
                                     cit.City.name))
