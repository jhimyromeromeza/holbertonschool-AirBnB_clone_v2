#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session, sessionmaker, scoped_session
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Manages storage of HBNB models in a MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Starting the engine """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
                f"mysql+mysqldb://{user}:{pwd}@{host}/{db}",
                pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Method that queries on the currect database session """
        db = {}
        all_classes = ['User', 'Review', 'Place', 'City', 'State']
        if cls is None:
            for cl in all_classes:
                cl = eval(cl)
                for instance in self.__session.query(cl).all():
                    key = instance.__class__.__name__ + '.' + instance.id
                    db[key] = instance
        else:
            for instance in self.__session.query(cls).all():
                key = instance.__class__.__name__ + '.' + instance.id
                db[key] = instance
        return db

    def new(self, obj):
        """ add object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes in the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete  the current database session """
        if obj is not None:
            self.__session.delete(obj)
            
    def close(self):
        self.__session.remove()
        self.reload()
        
    def reload(self):
        """ Reload  the database and new session """
        Base.metadata.create_all(self.__engine)
        session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fac)
        self.__session = Session()