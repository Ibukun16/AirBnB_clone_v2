#!/usr/bin/python3
""" State Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, MetaData
from sqlalchemy.orm import relationship, backref
import models
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """State class representation"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializing state"""
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """Getter function that obtains attribute that returns
            the instance City"""
            all_cities = models.storage.all("City")
            city = []
            for val in all_cities.values():
                if val.state_id == self.id:
                    city.append(val)
            return city
