#!/usr/bin/python3
"""
Contains the TestCityDocs classes
"""

from datetime import datetime
import inspect
from models import city
from models.base_model import BaseModel
import unittest
City = city.City


class TestCityDocs(unittest.TestCase):
    """test cases for class object Amenity"""
    @classmethod
    def setUpClass(cls):
        """test cases for class object Amenity"""
        cls.city_f = inspect.getmembers(City, inspect.isfunction)
        
    def test_city_module(self):
        """test cases for class object Amenity"""
        self.assertIsNot(city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py needs a docstring")
        
    def test_city_class(self):
        """test cases for class object Amenity"""
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")
        
    def test_city_func(self):
        """test cases for class object Amenity"""
        for func in self.city_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCity(unittest.TestCase):
    """test cases for class object Amenity"""
    def test_is_subclass(self):
        """test cases for class object Amenity"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_nam(self):
        """test cases for class object Amenity"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
        
    def test_st(self):
        """test cases for class object Amenity"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")
        
    def test_to_dic(self):
        """test cases for class object Amenity"""
        c = City()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in c.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict(self):
        """test cases for class object Amenity"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = City()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test cases for class object Amenity"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))
        
    if __name__ == "__main__":
        unittest.main()
