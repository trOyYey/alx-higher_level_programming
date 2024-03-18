#!/usr/bin/python3
""" prints all City objects from the database """
from model_city import City
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
    Base.metadata.create_all(engine)
    state_c = session.query(State, City).filter(State.id == City.state_id)
    for state, city in state_c:
        print(f'{state.name}: ({city.id}) {city.name}')
    session.commit()
    session.close()
