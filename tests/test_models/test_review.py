#!/usr/bin/python3
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_attributes(self):
        """Test Review attributes."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
