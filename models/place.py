#!/usr/bin/python3
from models import *
from models.base_model import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class PlaceAmenity(Base):
    __tablename__ = 'place_amenity'
    place_id = Column(String(60), ForeignKey('places.id'), primary_key=True)
    amenity_id = Column(String(60), ForeignKey('amenities.id'),
                        primary_key=True)


class Place(BaseModel):
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
