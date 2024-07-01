#!/usr/bin/python3
""" City Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), nullable=False,
                          ForeignKey("states.id"))
        places = relationship("Place", cascade="all, delete,
                              delete-orphan", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super.__init__(*args, **kwargs)
