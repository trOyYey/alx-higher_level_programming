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
    state_r = State(name="California")
    city_r = City(name="San Francisco")
    state_r.cities.append(city_r)
    session.add_all([city_r, state_r])
    session.commit()
    session.close()
