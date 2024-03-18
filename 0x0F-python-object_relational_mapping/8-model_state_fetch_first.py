#!/usr/bin/python3
""" list the first state objects from a database ordered by id """
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
    state = session.query(State).first()
    if state is not None:
        print(f'{state.id}: {state.name}')
    else:
        print('Nothing')
