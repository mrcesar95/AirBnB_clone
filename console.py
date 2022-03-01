#!/usr/bin/python3
"""
Class CommandConsole for Airbnb
"""
import cmd
from datetime import datetime

from click import prompt
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
import models

allowed_class = {"BaseModel": BaseModel, "Place": Place, "State": State,
                 "City": City, "Amenity": Amenity, "Review": Review,
                 "User": User}


class HBNBCommand(cmd.Cmd):
	"""
	HBNB Class
	"""
	prompt = '(hbnb) '
