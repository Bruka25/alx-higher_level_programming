#!/usr/bin/python3
"""python script that changes the name of the
   the state object where id = 2, to New
   Mexico
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

    reply = session.query(State).filter(State.id == 2)
    reply.update({"name": ("New Mexico")})

    session.commit()
