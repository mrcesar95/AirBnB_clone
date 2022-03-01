#!/usr/bin/python3
""" Creation of class base_model"""

from uuid import uuid4
from datetime import datetime

class BaseModel():
    """ Class BaseModel that defines all common
    attributes y methods"""
    def __init__(self):
        """ Initialization of class BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def __str__(self):
        """ Represntation string of class BaseModel"""
        __name = type(self).__name__
        return "[{}] ({}) {}".format(__name, self.id, self.__dict__)

    def save(self):
        """ Save the object into .json file"""
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """ return an dictionary representation of object"""
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
