#!/usr/bin/python3
from os import environ
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.engine import db_storage
from models.engine import file_storage

if environ.get('HBNB_TYPE_STORAGE') == 'db':
    storage = db_storage.DBStorage()
    storage.reload()
else:
    storage = file_storage.FileStorage()
    storage.reload()
