#!/usr/bin/python3
"""
Contains the TestCityDocs classes
"""

from datetime import datetime
import inspect
from models import amenity
from models.base_model import BaseModel
import unittest
Amenity = amenity.Amenity


class TestAmenityDocs(unittest.TestCase):
    """test cases for class object Amenity"""
    @classmethod
    def setUpClass(cls):
        """test cases for class object Amenity"""
        cls.city_f = inspect.getmembers(Amenity, inspect.isfunction)
        
    def test_city_module(self):
        """test cases for class object Amenity"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")
        
    def test_city_class(self):
        """test cases for class object Amenity"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")
                    
            
class TestAmenity(unittest.TestCase):
    """test cases for class object Amenity"""
    def test_is_subclass(self):
        """test cases for class object Amenity"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_nam(self):
        """test cases for class object Amenity"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
        
    def test_to_dic(self):
        """test cases for class object Amenity"""
        c = Amenity()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in c.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)
            
    def test_to_dict(self):
        """test cases for class object Amenity"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = Amenity()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))
        
    def test_str(self):
        """test cases for class object Amenity"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))
        
    if __name__ == "__main__":
        unittest.main()
