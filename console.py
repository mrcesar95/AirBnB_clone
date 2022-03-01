#!/usr/bin/python3
"""
Class CommandConsole for Airbnb
"""
import cmd
from datetime import datetime
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

	def do_quit(self, line):
		"""quit command: exit the program"""

	def do_EOF(self, line):
		"""End of File command: exit the program"""

	def emptyline(self):
		"""overridden to not do nothing"""
	pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
