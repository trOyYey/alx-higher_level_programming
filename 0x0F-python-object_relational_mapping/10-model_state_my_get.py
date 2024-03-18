#!/usr/bin/python3
""" list any state with matching input ordered by id """
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
    state_f = session.query(State).filter(State.name == sys.argv[4]).first()
    if state_f is None:
        print('Not found')
    else:
        print(state_f.id)
