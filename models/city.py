#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
import models
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    
    if getenv('HBNB_TYPE_STORAGE')=='db':
        state_id = column(str(60)9, nullable=False, foreignkey("state_id")
        name = column(str(128)), nullable=False
        
    else:
        name = ''
        state_id = ''
        
        

