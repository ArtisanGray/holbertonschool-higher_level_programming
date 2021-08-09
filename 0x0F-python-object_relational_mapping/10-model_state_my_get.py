#!/usr/bin/python3
"""manipulates data within sql database."""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state_name = str(sys.argv[4])
    state = session.query(State).order_by(State.id).filter(
                          State.name.contains(state_name)).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
