#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


if getenv("HBNB_TYPE_STORAGE") =="db":
    class State(BaseModel, Base):
        """class state"""
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

else:
    class State(BaseModel):
        name = ""



    @property
    def cities(self):
        l_cities = []
        for k in models.storage.all('City').values():
            if k.state_id == self.id:
                list_cities.append(k)
        return l_cities
