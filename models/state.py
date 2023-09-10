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

    if getenv("HBNB_TYPE_STORAGE") =="db":
        name = column(str(128)), nullable=False

    else:
         @property
    def cities(self):
      Zcity = []
      for city in models.storage.all('City').values():
        if city.state_id == self.id:
          Zcity.append(city)

    	return Zcity
