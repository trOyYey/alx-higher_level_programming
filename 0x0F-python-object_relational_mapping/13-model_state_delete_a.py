#!/usr/bin/python3
""" list any state containing letter 'a' from a database ordered by id """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}'
                           f'@localhost/{sys.argv[3]}',
                           pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    state_f = session.query(State).filter(State.name.like('%a%'))
    for state in state_f:
        session.delete(state)
    session.commit()
    session.close()
