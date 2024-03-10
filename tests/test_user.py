#!/usr/bin/python3
"""Module for the Place class."""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_attributes(self):
        """Test User attributes."""
        user = User()
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
