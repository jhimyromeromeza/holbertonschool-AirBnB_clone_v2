#!/usr/bin/python3

""" City Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship




class State(BaseModel, Base)
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") =="db":
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        @property
        def cities(self):
            "return the list of instances from City"
            from models import storage
            list_cities = []
            for k in models.storage.all('City').values():
                if k.state_id == self.id:
                    list_cities.append(k)
            return list_cities
