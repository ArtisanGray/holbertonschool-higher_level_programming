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
    first_state = session.query(State).filter(
                          State.name == sys.argv[4]).first()
    if first_state:
            print(first_state.id)
    else:
        print("Not found")
