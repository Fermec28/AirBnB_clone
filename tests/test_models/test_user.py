#!/usr/bin/python3
""" Test for User"""
import unittest
from models import storage
from models.user import User
import pep8

class TestUser(unittest.TestCase):
    '''Test BaseModel'''
    def setUp(self):
        self.my_model = User()

    def test_has_email_attribute(self):
        self.assertTrue(hasattr(User, "email"))

    def test_has_password_attribute(self):
        self.assertTrue(hasattr(User, "password"))

    def test_has_first_name_attribute(self):
        self.assertTrue(hasattr(User, "first_name"))

    def test_has_last_name_attribute(self):
        self.assertTrue(hasattr(User, "last_name"))

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
        document = User.__doc__
        self.assertIsNotNone(document)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
