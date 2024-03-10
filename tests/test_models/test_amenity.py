#!/usr/bin/python3
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_attributes(self):
        """Test Amenity attributes."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
