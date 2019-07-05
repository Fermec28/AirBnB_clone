#!/usr/bin/python3
""" Test for BaseModel"""
import unittest
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''Test BaseModel'''
    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "Holberton"
        self.my_model.my_number = 89
        self.my_model_json = self.my_model.to_dict()

    def test_doc_module(self):
        '''validate documentation module'''
        document = models.base_model.__doc__
        self.assertIsNotNone(document)

    def test_doc_module(self):
        '''validate documentation class'''
        document = BaseModel.__doc__
        self.assertIsNotNone(document)

    def test_has_attribute_id(self):
        '''test attribute'''
        self.assertTrue(hasattr(self.my_model, "id"))

    def test_has_attribute_created_at(self):
        '''test attribute'''
        self.assertTrue(hasattr(self.my_model, "created_at"))

    def test_has_attribute_updated_at(self):
        '''test attribute'''
        self.assertTrue(hasattr(self.my_model, "updated_at"))

    def test_has_attribute_save(self):
        '''test attribute'''
        self.assertTrue(hasattr(self.my_model, "save"))

    def test_has_attribute_class(self):
        '''test attribute'''
        self.assertTrue(hasattr(self.my_model_json, "__class__"))

    def test_values(self):
        '''test values'''
        self.assertAlmostEqual(self.my_model.name, "Holberton")
        self.assertAlmostEqual(self.my_model.my_number, 89)

    def test_exist(self):
        '''test attribute is not none'''
        self.assertIsNotNone(str(self.my_model))
        self.assertIsNotNone(self.my_model.to_dict())

    def test_save(self):
        '''test save attribute'''
        self.before = self.my_model.updated_at
        self.my_model.save()
        self.after = self.my_model.updated_at
        self.assertIsNot(self.before, self.after)

    def test_dict_method(self):
        '''test dict method'''
        self.my_model.name = "Holberton"
        self.my_model.my_number = 89
        dict_obj = self.my_model.to_dict()

        list_attr = ['id', 'created_at', 'updated_at', 'name',
                     'my_number', '__class__']

        nattr = 0
        for attr in dict_obj.keys():
            if attr in list_attr:
                nattr += 1
        self.assertAlmostEqual(6, nattr)

if __name__ == '__main__':
    unittest.main()
