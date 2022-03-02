#!/usr/bin/python3
""" Creation of class base_model"""

from uuid import uuid4
from datetime import datetime

class BaseModel():
    """ Class BaseModel that defines all common
    attributes y methods"""
    def __init__(self, *args, **kwargs):
        """ Initialization of class BaseModel"""
        if kwargs and len(kwargs) is not 0:
            del kwargs['__class__']
            for key, value in kwargs.items():
                setattr(self, key, value)
            self.updated_at = datetime.strptime(self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.created_at = datetime.strptime(self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
        if args is not None:
            pass
    
    def __str__(self):
        """ Representation string of class BaseModel"""
        __name = type(self).__name__
        return "[{}] ({}) {}".format(__name, self.id, self.__dict__)

    def save(self):
        """ Save the object into .json file"""
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """ return an dictionary representation of object"""
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        dictionary.update({'created_at' : self.created_at.isoformat(), 'updated_at' : self.updated_at.isoformat()})
        return dictionary
