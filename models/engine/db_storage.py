#!/usr/bin/python3
"""
Database storage engine using SQLAlchemy with a mysql+mysqldb
database connection.
"""
import os
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

class_name = {
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'State': State,
        'Review': Review,
        'User': User
    }


class DBStorage:
    """Representing the Storage Database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializing the object"""
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary of all the objects present"""
        if not self.__session:
            self.reload()
        objs = {}
        if cls:
            if type(cls) == str:
                cls = class_name.get(cls, None)
            for mem in self.__session.query(cls):
                key = mem.__class__.__name__ + '.' + mem.id
                objs[key] = mem
        else:
            for cname in class_name.values():
                for mem in self.__session.query(cname):
                    key = mem.__class__.__name__ + '.' + mem.id
                    objs[key] = mem
        return objs

    def get(self, cls, id):
        """obtain the object define by cls"""
        if cls is not None and type(cls) is str and id is not None\
                and type(id) is str and cls is class_name:
            cls = class_name[cls]
            res = self.__session.query(cls).filter(cls.id == id).first()
        else:
            return None

    def reload(self):
        """Reload objects from the database"""
        Base.metadata.create_all(self.__engine)
        maker = sessionmaker(bind=self.__engine,
                             expire_on_commit=False)
        self.__session = scoped_session(maker)

    def new(self, obj):
        """Creating a new object"""
        self.__session.add(obj)

    def save(self):
        """saving the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deleting an unwanted member from the table"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """Terminate the current session if active"""
        self.reload()
        self.__session.close()

    def count(self, cls=None):
        """obtain count of the objects in the storage"""
        summation = 0
        if type(cls) == str and cls in class_name:
            cls = class_name[cls]
            summation = self.__session.query(cls).count()
        elif cls is None:
            for cls in class_name.values():
                summation += self.__session.query(cls).count()
        return summation
