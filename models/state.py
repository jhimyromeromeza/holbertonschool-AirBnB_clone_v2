#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""
        cities = []
        
        @property
        def cities(self):
            """get a list of all related city instances
            with state_id = to the current state id
            """
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]