#!/usr/bin/python3
""" Test for User"""
import unittest
from models import storage
from models.place import Place
import pep8


class TestPlace(unittest.TestCase):
    '''Test Place'''
    def setUp(self):
        self.my_model = Place()

    def test_has_city_id_attribute(self):
        self.assertTrue(hasattr(Place, "city_id"))

    def test_has_user_id_attribute(self):
        self.assertTrue(hasattr(Place, "user_id"))

    def test_has_name_attribute(self):
        self.assertTrue(hasattr(Place, "name"))

    def test_has_description_attribute(self):
        self.assertTrue(hasattr(Place, "description"))

    def test_has_number_rooms_attribute(self):
        self.assertTrue(hasattr(Place, "number_rooms"))

    def test_has_number_bathrooms_attribute(self):
        self.assertTrue(hasattr(Place, "number_bathrooms"))

    def test_has_max_guest_attribute(self):
        self.assertTrue(hasattr(Place, "max_guest"))

    def test_has_price_by_night_attribute(self):
        self.assertTrue(hasattr(Place, "price_by_night"))

    def test_has_latitude_attribute(self):
        self.assertTrue(hasattr(Place, "latitude"))

    def test_has_longitude_attribute(self):
        self.assertTrue(hasattr(Place, "longitude"))

    def test_has_amenity_ids_attribute(self):
        self.assertTrue(hasattr(Place, "amenity_ids"))

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
        document = Place.__doc__
        self.assertIsNotNone(document)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
