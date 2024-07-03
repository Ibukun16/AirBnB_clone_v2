#!/usr/bin/python3
""" Place Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table 
from sqlalchemy.orm import relationship


if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ Representation of a place to stay """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")
    
    def __init__(self, *args, **kwargs):
        """Initializing Place"""
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """attribute that returns list of  Review instances"""
            review_val = models.storage.all("Review").values()
            review = []
            for r in review_val:
                if r.place_id == self.id:
                    review.append(r)
            return review

        @property
        def amenities(self):
            """attribute that returns list of Amenity instances"""
            amenity_val = models.storage.all("Amenity").values()
            amenity_list = []
            for item in amenity_val:
                if item.place_id == self.id:
                    amenity_list.append(mem)
            return amenity_list

        @amenities.setter
        def amenities(self, obj=None):
            """Setter attribute that add Amenity to amenity_ids"""
            if type(obj) == Amenity and obj.id != self.amenity_ids:
                self.amenity_ids.append(obj.id)
