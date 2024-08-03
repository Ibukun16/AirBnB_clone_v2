#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
import models
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, MetaData
from sqlalchemy.orm import relationship, backref


class Amenity(BaseModel, Base):
    """Representation of the Amenity class"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       viewonly=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializing Amenity"""
        super().__init__(*args, **kwargs)
