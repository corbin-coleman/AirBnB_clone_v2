#!/usr/bin/python3
from models import *
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel):
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey("places.id"))
    user_id = Column(String(60), ForeignKey("users.id"))
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
