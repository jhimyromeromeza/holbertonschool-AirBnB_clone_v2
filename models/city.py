#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
import models
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, foreignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    
    if os.getenv('HBNB_TYPE_STORAGE')=='db':
        __tablename__ = 'cities'
        state_id = Column(String(60), nullable=False, Foreignkey("state_id"))
        name = Column(String(128), nullable=False)
        
    else:
        name = ''
        state_id = ''
        
        

