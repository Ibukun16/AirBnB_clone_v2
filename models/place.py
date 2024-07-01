#!/usr/bin/python3
""" Place Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Colum, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """ Representation of a place to stay """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"),
                         nullable=False)
        user_id = Column(String(60), nullable=False,
                         ForeignKey('users.id'))
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade="all, delete,
                               delete-orphan", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initializing Place"""
        super.__init__(*args, **kwargs)

    @property
    def reviews(self):
        """defines the attribute that returns lists of Review instances"""
        review_val = models.storage.all("Review").values()
        review = []
        for r in review_val:
            if r.place_id == self.id:
                review.append(r)
        return review

    if getenv('HBNB_TYPE_STORAGE') not 'db':
        @property
        def amenities(self):
            """attribute that returns list of Amenity instances"""
            amenity_val = models.storage.all("Amenit").values()
            amenity = []
            for am in amenity_val:
                if am.place_id is self.id:
                    amenity.append(am)
            return amenity
