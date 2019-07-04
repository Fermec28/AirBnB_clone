#!/usr/bin/python3
""" Test for City"""
import unittest
from models import storage
from models.city import City
import pep8


class TestUser(unittest.TestCase):
    '''Test State'''
    def setUp(self):
        self.my_model = City()

    def test_has__name_attribute(self):
        self.assertTrue(hasattr(City, "name"))

    def test_has__state_id_attribute(self):
        self.assertTrue(hasattr(City, "state_id"))

    def test_has_id_attribute(self):
        self.assertTrue(hasattr(self.my_model, "id"))

    def test_has_created_at__attribute(self):
        self.assertTrue(hasattr(self.my_model, "created_at"))

    def test_has_updated_at__attribute(self):
        self.assertTrue(hasattr(self.my_model, "updated_at"))

    def test_has_updated_at__attribute(self):
        self.assertTrue(hasattr(self.my_model, "save"))

    def test_doc_module(self):
        '''validate documentation module'''
        document = models.review.__doc__
        self.assertIsNotNone(document)

    def test_doc_module(self):
        '''validate documentation class'''
        document = City.__doc__
        self.assertIsNotNone(document)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
