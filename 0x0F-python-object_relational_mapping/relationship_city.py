#!/usr/bin/python3
""" City Class """
from relationship_state import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey


class City(Base):
    """
    City subclass
    defining using Object rational mapping

    Attributes:
        id: unique id for each city used as primary key
        name: name of the city
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
