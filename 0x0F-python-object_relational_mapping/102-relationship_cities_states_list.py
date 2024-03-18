#!/usr/bin/python3
""" prints all City objects from the database """
from relationship_city import City
import sys
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}'
                           f'@localhost/{sys.argv[3]}',
                           pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    state_c = session.query(State).order_by(State.id)
    for state in state_c:
        for city in state.cities:
            print(f'{city.id}: {city.name} -> {state.name}')
    session.close()
