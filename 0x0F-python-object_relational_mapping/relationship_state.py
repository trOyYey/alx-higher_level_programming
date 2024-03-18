#!/usr/bin/python3
""" State Class definition Using relationships """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    State class sub class from Base

    Attributes:
        id: state.id in MySQL table
        name: state.name in MySQL table
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade='all, delete')
