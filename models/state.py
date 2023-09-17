#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
else:
    class State(BaseModel):
        name = ""
        
        @property
        def cities(self):
            """get a list of all related city instances
            with state_id = to the current state id
            """
            from models.city import City
            list_cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities