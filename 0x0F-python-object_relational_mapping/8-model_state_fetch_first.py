#!/usr/bin/python3
"""fetches a state from new table class"""
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
