#!/usr/bin/python3
"""Python script for printing the first state
   pbject using sqlalchemy
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    reply = session.query(State.id, State.name).first()
    if (reply is None):
        print("Nothing")
    else:
        print("{:d}: {}".format(reply[0], reply[1]))
