#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from os import getenv


class Amenity(BaseModel):
    """Representation of the Amenity class"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       back_populates="amenities")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Inherited init"""
        super.__init__(*args, **kwargs)
