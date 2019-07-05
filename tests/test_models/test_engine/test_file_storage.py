#!/usr/bin/python3
""" Test for BaseModel"""
import unittest
import models
import pep8

class TestFileStorage(unittest.TestCase):
    '''Test FileStorage'''
    def setUp(self):
        pass

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
