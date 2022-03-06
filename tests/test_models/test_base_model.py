#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test Base Model"""

from models.base_model import BaseModel
import models
from datetime import datetime
import unittest
import os
from time import sleep


class Test_BaseModel(unittest.TestCase):

    """Test Base model"""

    @classmethod
    def setUp(self):
        """ setup"""
        self.ritmobase = BaseModel()

    def tearDown(self):
        """tearDown"""
        if os.path.exists("file.json"):
            os.remove("file.json")
            
    def test_createinstance(self):
        """create instance"""
        ritmobase = BaseModel()
        self.assertEqual(type(ritmobase.id), str)
        self.assertEqual(type(ritmobase.created_at), datetime)
        self.assertEqual(type(ritmobase.updated_at), datetime)

    def test_idiferent(self):
        """id diferetent"""
        ritmobase1 = BaseModel(69)
        self.assertNotEqual(ritmobase1.id, 69)
        ritmobase1 = BaseModel("hi")
        self.assertNotEqual(ritmobase1.id, "hi")
        ritmobase1 = BaseModel([0, 1, 2])
        self.assertNotEqual(ritmobase1.id, [0, 1, 2])

    def test_cuandosecreopadre(self):
        """la puta que lo aprio"""
        ritmobase2 = BaseModel()
        self.assertEqual(type(ritmobase2.created_at), type(datetime.now()))
        self.assertTrue(hasattr(ritmobase2, "created_at"))
        
    def test_update(self):
        """update"""
        ritmobase2 = BaseModel()
        self.assertEqual(type(ritmobase2.updated_at), type(datetime.now()))
        self.assertTrue(hasattr(ritmobase2, "updated_at"))
        actualizado = ritmobase2.updated_at
        self.assertTrue(actualizado == ritmobase2.updated_at)
        ritmobase2.save()
        self.assertFalse(actualizado == ritmobase2.updated_at)
        
    def test_severalinstances(self):
        """Several instances"""
        ritmobase = BaseModel()
        self.assertEqual(type(ritmobase.id), str)
        self.assertEqual(type(ritmobase.created_at), datetime)
        self.assertEqual(type(ritmobase.updated_at), datetime)
        ritmobase1 = BaseModel()
        self.assertEqual(type(ritmobase1.id), str)
        self.assertEqual(type(ritmobase1.created_at), datetime)
        self.assertEqual(type(ritmobase1.updated_at), datetime)
        ritmobase2 = BaseModel()
        self.assertEqual(type(ritmobase2.id), str)
        self.assertEqual(type(ritmobase2.created_at), datetime)
        self.assertEqual(type(ritmobase2.updated_at), datetime)
        self.assertNotEqual(ritmobase.id, ritmobase1.id, ritmobase2.id)
        
    def test_addatributes(self):
        """Add atributes"""
        ritmobase = BaseModel()
        ritmobase.name = "Elizabeth"
        ritmobase.my_number = 69
        pictionario = ritmobase.to_dict()
        self.assertEqual('name' in pictionario, True)
        self.assertEqual('my_number' in pictionario, True)
        ritmobase1 = BaseModel()
        pictionario2 = ritmobase1.to_dict()
        self.assertEqual('name' in pictionario2, False)
        self.assertEqual('my_number' in pictionario2, False)
        
    def test_metodostring(self):
        """method string"""
        ritmobase = BaseModel()
        self.assertEqual(type(str(ritmobase)), str)
        
    def test_metstrclasname(self):
        """class name"""
        ritmobase = BaseModel()
        self.assertEqual('[BaseModel]' in str(ritmobase), True)
    
    def test_strid(self):
        """str id"""
        ritmobase = BaseModel()
        self.assertEqual('id' in str(ritmobase), True)
        
    def test_strcreatedat(self):
        """str created at"""
        ritmobase = BaseModel()
        self.assertEqual('created_at' in str(ritmobase), True)

    def test_strupdatedat(self):
        """str update at"""
        base = BaseModel()
        self.assertEqual('updated_at' in str(base), True)
        
    def test_print(self):
        """print"""
        base = BaseModel()
        result = "[{}] ({}) {}".format(
        base.__class__.__name__,
            base.id,
            base.__dict__
        )
        self.assertEqual(result, str(base))

    def test_save(self):
        """save"""
        ritmobase = BaseModel()
        tiempopachu = ritmobase.updated_at
        sleep(10)
        ritmobase.id = 69
        ritmobase.save()
        tiempokiko = ritmobase.updated_at
        self.assertTrue(hasattr(ritmobase, "id"))
        self.assertTrue(ritmobase.id == 69)
        self.assertNotEqual(tiempokiko, tiempopachu)
        with open("file.json", "r", encoding="utf-8") as f:
            self.assertTrue("\"id\": 69" in f.read())
            
    def test_todict(self):
        """Dictionary"""
        var = BaseModel()
        self.assertEqual(type(var.to_dict()), dict)

    def test_updatedatsave(self):
        """update save"""
        var = BaseModel()
        var.save()
        self.assertEqual(type(var.updated_at), type(datetime.now()))
        self.assertEqual(type(var.updated_at), datetime)
        self.assertTrue(hasattr(var, "updated_at"))
    
    def test_dicttoatsall(self):
        """dictionary"""
        var = BaseModel()
        dictionary = var.to_dict()
        self.assertEqual('__class__' in dictionary, True)
        self.assertEqual('id' in dictionary, True)
        self.assertEqual('created_at' in dictionary, True)
        self.assertEqual('updated_at' in dictionary, True)

    def test_arg(self):
        """arg"""
        with self.assertRaises(NameError) as a:
            var = BaseModel(ea)
            self.assertEqual(str(a.exception), "name 'ea' is not defined")

    def test_toomanyargs(self):
        """too many args"""
        with self.assertRaises(TypeError) as a:
            var = BaseModel()
            var.save("eae")
            self.assertEqual(str(a.exception), "save() takes 1 positional" +
                             " argument but 2 were given")

    def test_saveint(self):
        """save int"""
        var1 = BaseModel()
        with self.assertRaises(TypeError) as a:
            var1.save(69)
            
            self.assertEqual(str(a.exception), "save() takes 1 positional" +
                             " argument but 2 were given")
            
    def test_Toomanyargumentsfather(self):
        """more args father"""
        with self.assertRaises(TypeError) as a:
            var = BaseModel()
            var.to_dict("eae")
            self.assertEqual(str(a.exception), "to_dict() takes 1 positional" +
                             " argument but 2 were given")
    if __name__ == "__main__":
        unittest.main()
