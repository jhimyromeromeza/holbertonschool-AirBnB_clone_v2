#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import getenv
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.base_model import BaseModel
from models.amenity import Amenity


storage = gateenv('HBNB_TYPE_STORAGE')

if storage == db:
    from models.engine.file_storage import FileStorage
    storage.DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()


storage.reload()
