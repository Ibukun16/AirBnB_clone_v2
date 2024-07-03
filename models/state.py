#!/usr/bin/python3
""" State Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """State class representation"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")


    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """Getter function that obtains attribute that returns
            the instance City"""
            city_val = models.storage.all("City").values()
            city = []
            for val in city_val:
                if val.state_id == self.id:
                    city.append(c)
            return city
