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


class DBStorage(models):
    """Class DBSTORAGE"""
    __engine = "None"
    __session = "None"

    def __init__(self):
        """IMPORTING ENVIROMENT VARIABLES"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = gatenv('HBNB_MYSQL_HOST')
        db = gatenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{pwd}@{host}/{db}",
            pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Method that queries on the currect database session """
        objects = {}
        if cls is None:
            clas_name = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']

            for class_name in class_names:
                class_obj = getattr(models, class_name)
                all_objects = self.__session.query(class_obj).all()
                objects_dict = {
                        f"{class_name}.{obj.id}": obj for obj in all_objects}
                objects.update(objects_dict)
        else:
            class_cls = self.__session.query(cls).all()
            objects = {
                    f"{type(obj).__name__}.{obj.id}": obj for obj in class_cls}

    def new(self, obj):
        """add the current data base session"""
        self.__session.add(obj)

    def save(self):
        """save the current data base session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete the current data base session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """commit all the change in databse"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """close all the changes in database"""
        self.__session.close()
