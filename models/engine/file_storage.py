#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj is not None:
            to_obj = obj.__class__.__name__ + '.' +obj.id
            self.__objects[to_obj] = obj

    def save(self):
        dictionary = {}
        for key in self.__objects:
            dictionary[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dictionary,f)
            
    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    value = ast.literal_eval(value['__class__'])(**value)
                    self.__objects[key] = value
        except:
            pass
