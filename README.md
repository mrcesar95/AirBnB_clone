AirBnB Clone.
The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

hbnb

General
How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function

Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7 or more)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c ‘print(import(“my_module”).doc)’)
All your classes should have a documentation (python3 -c ‘print(import(“my_module”).MyClass.doc)’)
All your functions (inside and outside a class) should have a documentation (python3 -c ‘print(import(“my_module”).my_function.doc)’ and python3 -c ‘print(import(“my_module”).MyClass.my_function.doc)’)
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

Python Unit Tests
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
You have to use the unittest module
All your test files should be python files (extension: .py)
All your test files and folders should start by test_
Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
All your modules should have a documentation (python3 -c ‘print(import(“my_module”).doc)’)
All your classes should have a documentation (python3 -c ‘print(import(“my_module”).MyClass.doc)’)
All your functions (inside and outside a class) should have a documentation (python3 -c ‘print(import(“my_module”).my_function.doc)’ and python3 -c ‘print(import(“my_module”).MyClass.my_function.doc)’)
We strongly encourage you to work together on test cases, so that you don’t miss any edge case

Unittests
We did the testing of our classes with the unittest module, making sure that we do not have any case left without considering

Console.
Objetives
The objective of the console is mainly to be able to control the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object
Commands
quit or EOF exit the program. Ex:
(hbnb) quit
root@7e0c3c33ccb3:~/airbnb#
help displays a brief description of the specified command. Ex:
(hbnb) help

Documented commands (type help <topic>):
EOF all create destroy help quit show update

(hbnb)
create create a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex:
(hbnb) create User
63bdfac2-cff1-465f-81b0-41e00bd1af17
show prints the string representation of an instance based on the class name and id. Ex:
(hbnb) show User 63bdfac2-cff1-465f-81b0-41e00bd1af17
[User] (63bdfac2-cff1-465f-81b0-41e00bd1af17) {‘id’: ‘63bdfac2-cff1-465f-81b0-41e00bd1af17’, ‘updated_at’: datetime.datetime(2021, 6, 26, 1, 34, 37, 393154), ‘created_at’: datetime.datetime(2021, 6, 26, 1, 34, 37, 392708)}
(hbnb)
destroy deletes an instance based on the class name and id (save the change into the JSON file). Ex:
(hbnb) destroy User 63bdfac2-cff1-465f-81b0-41e00bd1af17
(hbnb)
all prints all string representation of all instances based or not on the class name. Ex:
(hbnb) all User
[[User] (0fed14f5-df97-413f-9686-c55a6741c687) {‘id’: ‘0fed14f5-df97-413f-9686-c55a6741c687’, ‘updated_at’: datetime.datetime(2021, 6, 26, 0, 57, 4, 16982), ‘created_at’: datetime.datetime(2021, 6, 26, 0, 57, 4, 16478)}]
(hbnb)
update Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex:
(hbnb) update User 0fed14f5-df97-413f-9686-c55a6741c687 email "aibnb@holbertonschool.com"
(hbnb) show User 0fed14f5-df97-413f-9686-c55a6741c687
[User] (0fed14f5-df97-413f-9686-c55a6741c687) {‘id’: ‘0fed14f5-df97-413f-9686-c55a6741c687’, ‘created_at’: datetime.datetime(2021, 6, 26, 0, 57, 4, 16478), ‘updated_at’: datetime.datetime(2021, 6, 26, 1, 41, 52, 402202), ‘email’: ‘aibnb@holbertonschool.com’}
(hbnb)
init
Python file that create a unique FileSotrage instance for it application. It contains:

import file_storage.py
create the variable storage, an instance of FileStorage
call reload() method on this variable

BaseModel
We create a base class called BaseModel, from which the rest of the more specific classes will inherit. In this class all common attributes and methods were defined.

Initialize with init(self, *args, **kwargs)
Where *args does not exist and **kwargs will be used to save the created objects in a .json file
if it’s a new instance (not from a dictionary representation), call to the method new(self) on storage

Public instance attributes:
id assigned with an uuid when an instance is created
created_at: datetime - assign with the current datetime when an instance is created
updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
str: should print: [<class name>] (<self.id>) <self.dict>
Public instance methods:
save(self): updates the public instance attribute updated_at with the current datetime
call save(self) method of storage
to_dict(self): returns a dictionary containing all keys/values of dict of the instance:

FileStorage
We create a FileStorage class that serializes instances to a JSON file and deserializes JSON file to instances:

Private class attributes:
__file_path: string - path to the JSON file (ex: file.json)
__objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
Public instance methods:
all(self): returns the dictionary __objects
new(self, obj): sets in __objects the obj with key <obj class name>.id
save(self): serializes __objects to the JSON file (path: __file_path)
reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
Inherited objects from BaseModel
We have added different classes that will be used in future projects with their respective public attributes:

User
email: string - empty string
password: string - empty string
first_name: string - empty string
last_name: string - empty string

State
name: string - empty string

City
state_id: string - empty string: it will be the State.id
name: string - empty string

Amenity
name: string - empty string

Place
city_id: string - empty string: it will be the City.id
user_id: string - empty string: it will be the User.id
name: string - empty string
description: string - empty string
number_rooms: integer - 0
number_bathrooms: integer - 0
max_guest: integer - 0
price_by_night: integer - 0
latitude: float - 0.0
longitude: float - 0.0
amenity_ids: list of string - empty list: it will be the list of Amenity.id later

Review
place_id: string - empty string: it will be the Place.id
user_id: string - empty string: it will be the User.id
text: string - empty string
### Author
***
*Holberton School Student*

Elizabeth González Payares  - [Github](https://github.com/Artemisse99) - [Twiter](https://twitter.com/Elizabe57763803)

Cesar Molina  - [Github]() - [Twiter]("")
