""" Test for Review"""
import unittest
from models import storage
from models.review import Review
import pep8

class TestReview(unittest.TestCase):
    '''Test BaseModel'''
    def setUp(self):
        self.my_model = Review()

    def test_has_place_id_attribute(self):
        self.assertTrue(hasattr(Review, "place_id"))

    def test_has_user_id_attribute(self):
        self.assertTrue(hasattr(Review, "user_id"))

    def test_has_text_attribute(self):
        self.assertTrue(hasattr(Review, "text"))

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
        document = Review.__doc__
        self.assertIsNotNone(document)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
