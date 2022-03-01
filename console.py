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
		return True

	def do_EOF(self, line):
		"""End of File command: exit the program"""
		return True

	def emptyline(self):
		"""overridden to not do nothing"""
	pass

	# def precmd(self, line):
	# 	"""Edit given command to allow second type of input"""
	# 	split_line = line.split("(")
	# 	flag_instance = 0
	# 	if(len(split_line) > 1):
	# 		tmp = split_line[0].split(".", 1)
	# 		flag_instance = 1
		
	def do_create(self, line):
		"""Create a new instance of BaseModel, saves it (to the JSON file 
		and prints the id"""
		if len(line) == 0:
			print("** class name missing **")
			return
		try:
			string = line + "()"
			instance = eval(string)
			print(instance.id)
			instance.save()
		except Exception as f:
			print("** class doesn't exist **")
	
	def do_show(self, line):
		"""Prints the string representation of an instance
		based on the class name nd id.
		Ex: $ show BaseModel 1234-1234-1234."""
		cmd_line = line.split()
		if len(cmd_line) == 0:
			print("** class name missing **")
			return
		elif cmd_line[0] not in allowed_class.keys():
			print("** class doesn't exist **")
		elif len(cmd_line) == 1:
			print("** instance id missing **")
		elif len(cmd_line) == 2:
			instance = cmd_line[0] + "." + cmd_line[1]
			if instance in models.storage.all():
				print(models.storage.all()[instance])
			else:
				print("**no instance found **")
		



if __name__ == '__main__':
    HBNBCommand().cmdloop()
