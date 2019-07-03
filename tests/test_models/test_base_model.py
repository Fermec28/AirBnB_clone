#!/usr/bin/python3
""" Test for User"""
import unittest
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    '''Test BaseModel'''
    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "Holberton"
        self.my_model.my_number = 89
        self.my_model_json = self.my_model.to_dict()

    def test_has_attribute(self):
        self.assertTrue(hasattr(self.my_model, "id"))
        self.assertTrue(hasattr(self.my_model, "created_at"))
        self.assertTrue(hasattr(self.my_model, "updated_at"))
        self.assertTrue(hasattr(self.my_model_json, "__class__"))

    def test_values(self):
        self.assertAlmostEqual(self.my_model.name, "Holberton")
        self.assertAlmostEqual(self.my_model.my_number, 89)
        self.assertIsNotNone(str(self.my_model))
        self.assertIsNotNone(self.my_model.to_dict())


if __name__ == '__main__':
    unittest.main()
