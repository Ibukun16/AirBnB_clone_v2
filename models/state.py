#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class representation"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete,
                          delete-orphan", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializing the state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Getter function that obtains attribute that returns
            the instance City"""
            city_val = models.storage.all("City").values()
            city = []
            for c in city_val:
                if c.state_id is self.id:
                    city.append(c)
            return city
