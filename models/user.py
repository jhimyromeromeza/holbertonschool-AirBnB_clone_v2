#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from models.base_model import Base
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places  = relationship("Place", cascade="all, delete, delete-orphan", backref="user")
        reviews = relationship("Review", cascade="all, delete, delete-orphan", backref="user")
