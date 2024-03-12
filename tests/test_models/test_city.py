#!/usr/bin/python3
"""Unit tests for the City class."""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_instance_creation(self):
        """Test creation of a new City instance."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))

    def test_attributes(self):
        """Test initialization of City attributes."""
        city = City(name="New York", state_id="NY")
        self.assertEqual(city.name, "New York")
        self.assertEqual(city.state_id, "NY")

    def test_str_representation(self):
        """Test the __str__ method of City."""
        city = City(name="New York", state_id="NY")
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)


if __name__ == '__main__':
    unittest.main()
